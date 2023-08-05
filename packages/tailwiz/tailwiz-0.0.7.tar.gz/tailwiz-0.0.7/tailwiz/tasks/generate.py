import evaluate
import os
os.environ['TRANSFORMERS_CACHE'] = 'cache'  # Must be before transformers import.
import pandas as pd
import torch
import transformers
from sklearn.model_selection import train_test_split

from .task import Task

class GenerateTask(Task):
    def __init__(self, train, val, test):
        (
            self.train_dataset,
            self.val_dataset,
            self.val_references,
            self.test_dataset
        ) = self._load_data(train, val, test)
        self.model = self._load_model()

    def _load_data(self, train, val, test):
        self.tokenizer = transformers.T5Tokenizer.from_pretrained('google/flan-t5-base', cache_dir='cache/flan-t5')
        
        train_tokens = None
        if train:
            train_tokens = self.tokenizer([t[0] for t in train], return_tensors='pt', padding=True)
            train_labels = self.tokenizer([t[1] for t in train], return_tensors='pt', padding=True)
            train_tokens['labels'] = train_labels['input_ids']
        
        val_tokens = None
        if val:
            val_tokens = self.tokenizer([v[0] for v in val], return_tensors='pt', padding=True)
            val_labels = self.tokenizer([v[1] for v in val], return_tensors='pt', padding=True)
            val_tokens['labels'] = val_labels['input_ids']

        test_tokens = self.tokenizer(test, return_tensors='pt', padding=True)

        return train_tokens, val_tokens, [v[1] for v in val], test_tokens

    def _load_model(self):
        return transformers.T5ForConditionalGeneration.from_pretrained('google/flan-t5-base', cache_dir='cache/flan-t5')

    def train(self):
        class FT5Dataset(torch.utils.data.Dataset):
            def __init__(self, data):
                self.data = data
            
            def __len__(self):
                return len(self.data['input_ids'])
            
            def __getitem__(self, index):
                return {k: self.data[k][index] for k in self.data.keys()}

        args = transformers.Seq2SeqTrainingArguments(
            'cache/flan-t5',
            num_train_epochs=15,
            evaluation_strategy='epoch',
            save_strategy='epoch',
            load_best_model_at_end=True,
            predict_with_generate=True,
            metric_for_best_model='eval_loss',
            logging_steps=1,
        )
        trainer = transformers.Seq2SeqTrainer(
            model=self.model,
            args=args,
            train_dataset=FT5Dataset(self.train_dataset),
            eval_dataset=FT5Dataset(self.val_dataset) if self.val_dataset is not None else FT5Dataset(self.train_dataset),  # Requires eval dataset.
        )
        trainer.train()

    def evaluate(self):
        # Remove 'labels' key from validation dataset for prediction.
        dummy_val = self.val_dataset.copy()
        del dummy_val['labels']
        outputs = self.model.to(dummy_val['input_ids'].device).generate(**dummy_val)
        predictions = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)

        metrics_funcs = [
            evaluate.load('exact_match'),
            evaluate.load('rouge')
        ]
        metrics = {}
        for metric in metrics_funcs:
            metrics.update(metric.compute(predictions=predictions, references=self.val_references))
        for k in metrics.keys():
            metrics[k] = metrics[k].item()
        return metrics

    def predict(self):
        outputs = self.model.to(self.test_dataset['input_ids'].device).generate(**self.test_dataset)
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)


def generate(text_to_label, prelabeled_text=None, output_metrics=False):
    if isinstance(text_to_label, pd.DataFrame):
        assert 'prompt' in text_to_label.columns, \
            'Make sure the prompt column in your pandas DataFrame is named "prompt".'
        text_to_label = text_to_label.prompt.tolist()
    if isinstance(prelabeled_text, pd.DataFrame):
        assert 'prompt' in prelabeled_text.columns and 'label' in prelabeled_text.columns, \
            'Make sure the prompt column in your pandas DataFrame is named "prompt" and the label column is named "label".'
        prelabeled_text = list(zip(prelabeled_text.prompt.tolist(), prelabeled_text.label.tolist()))
    if output_metrics:
        assert prelabeled_text is not None, 'In order to output an estimate of performance with output_metrics, prelabeled_text must be provided.'

    if prelabeled_text is None:
        generate_task_out = GenerateTask([], [], text_to_label)
        results = generate_task_out.predict()
    else:
        assert len(prelabeled_text) >= 2, 'At least 2 rows of prelabeled data must be given.'
        train, val = train_test_split(prelabeled_text, test_size=0.2)
        generate_task_out = GenerateTask(train, val, text_to_label)
        generate_task_out.train()
        results = generate_task_out.predict()

    if output_metrics:
        metrics = generate_task_out.evaluate()

    return (results, metrics) if output_metrics else results
