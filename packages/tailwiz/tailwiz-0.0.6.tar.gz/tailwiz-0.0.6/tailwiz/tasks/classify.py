import numpy as np
import os
os.environ['TRANSFORMERS_CACHE'] = 'cache'  # Must be before transformers import.
import pandas as pd
import sklearn
from sklearn import cluster, linear_model, metrics, multiclass
from sklearn.model_selection import train_test_split
import torch
import transformers

from . import utils
from .task import Task


class BinaryClassificationTask(Task):
    def __init__(self, train, val, test):
        (
            self.train_embeds,
            self.train_labels,
            self.val_embeds,
            self.val_labels,
            self.test_embeds
        ) = self._load_data(train, val, test)
        self.model = self._load_model()

    def _load_data(self, train, val, test):
        text = [x[0] for x in train] + [x[0] for x in val] + test  # Must embed togeter to match sequence length.

        # Tokenize.
        tokenizer = transformers.BertTokenizer.from_pretrained('bert-base-uncased')
        token_ids = tokenizer(text, return_tensors='pt', padding=True)
        
        # Embed.
        embed_model = transformers.BertModel.from_pretrained('bert-base-uncased')
        embed_model.eval()
        with torch.no_grad():
            embeds = embed_model(**token_ids)[0]
        embeds = embeds.mean(axis=1)

        return embeds[:len(train)], [x[1] for x in train], embeds[len(train):len(train) + len(val)], [x[1] for x in val], embeds[len(train) + len(val):]

    def _load_model(self):
        return linear_model.LogisticRegression(random_state=0, max_iter=1000)

    def train(self):
        self.model.fit(self.train_embeds, self.train_labels)

    def evaluate(self):
        if len(self.val_embeds) == 0:
            return None

        val_preds = self.model.predict(self.val_embeds)
        val_probs = self.model.predict_proba(self.val_embeds)

        acc = metrics.accuracy_score(self.val_labels, val_preds).item()
        prec = metrics.precision_score(self.val_labels, val_preds, zero_division=0).item()
        rec = metrics.recall_score(self.val_labels, val_preds, zero_division=0).item()
        f1 = metrics.f1_score(self.val_labels, val_preds, zero_division=0).item()

        fpr, tpr, _ = metrics.roc_curve(self.val_labels, val_probs[:,1])
        auroc = metrics.auc(fpr, tpr).item()

        precision, recall, _ = metrics.precision_recall_curve(self.val_labels, val_probs[:,1])
        aupr = metrics.auc(recall, precision).item()

        return {
            'acc': acc,
            'prec': prec,
            'rec': rec,
            'f1': f1,
            'metrics@90rec': utils.metrics_at_recall(0.9, val_probs[:,1].tolist(), self.val_labels),
            'metrics@95rec': utils.metrics_at_recall(0.95, val_probs[:,1].tolist(), self.val_labels),
            'metrics@99rec': utils.metrics_at_recall(0.99, val_probs[:,1].tolist(), self.val_labels),
            'auroc': auroc,
            'aupr': aupr,
        }

    def predict(self):
        return self.model.predict(self.test_embeds).tolist()


class MulticlassClassificationTask(BinaryClassificationTask):
    def __init__(self, train, val, test):
        (
            self.train_embeds,
            self.train_labels,
            self.val_embeds,
            self.val_labels,
            self.test_embeds
        ) = self._load_data(train, val, test)

        self.classes = list(set(self.train_labels + self.val_labels))
        self.train_labels = sklearn.preprocessing.label_binarize(self.train_labels, classes=self.classes).tolist()
        if len(self.val_labels) > 0:
            self.val_labels = sklearn.preprocessing.label_binarize(self.val_labels, classes=self.classes).tolist()

        self.model = self._load_model()
    
    def _load_data(self, train, val, test):
        return super()._load_data(train, val, test)

    def _load_model(self):
        return multiclass.OneVsRestClassifier(linear_model.LogisticRegression(random_state=0, max_iter=1000))
    
    def train(self):
        return super().train()

    def evaluate(self):
        if len(self.val_embeds) == 0:
            return None

        val_preds = self.model.predict(self.val_embeds)
        val_probs = self.model.predict_proba(self.val_embeds)

        accs = {}
        precs = {}
        recs = {}
        f1s = {}
        metrics_at_90rec = {}
        metrics_at_95rec = {}
        metrics_at_99rec = {}
        aurocs = {}
        auprs = {}

        # Get one-vs-all classification metrics for each class.
        for i, class_name in enumerate(self.classes):
            class_bin = [0 for _ in range(len(self.classes))]
            class_bin[i] = 1

            labels_bin = [1 if j == class_bin else 0 for j in self.val_labels]
            preds_bin = [1 if j == class_bin else 0 for j in val_preds.tolist()]

            accs[class_name] = metrics.accuracy_score(labels_bin, preds_bin).item()
            precs[class_name] = metrics.precision_score(labels_bin, preds_bin, zero_division=0).item()
            recs[class_name] = metrics.recall_score(labels_bin, preds_bin, zero_division=0).item()
            f1s[class_name] = metrics.f1_score(labels_bin, preds_bin, zero_division=0).item()
            metrics_at_90rec[class_name] = utils.metrics_at_recall(0.9, val_probs[:, i].tolist(), labels_bin)
            metrics_at_95rec[class_name] = utils.metrics_at_recall(0.95, val_probs[:, i].tolist(), labels_bin)
            metrics_at_99rec[class_name] = utils.metrics_at_recall(0.99, val_probs[:, i].tolist(), labels_bin)


            fpr, tpr, _ = metrics.roc_curve(labels_bin, val_probs[:,i])
            aurocs[class_name] = metrics.auc(fpr, tpr).item()

            precision, recall, _ = metrics.precision_recall_curve(labels_bin, val_probs[:,i])
            auprs[class_name] = metrics.auc(recall, precision).item()

        return {
            'acc': accs,
            'prec': precs,
            'rec': recs,
            'f1': f1s,
            'metrics@90rec': metrics_at_90rec,
            'metrics@95rec': metrics_at_95rec,
            'metrics@99rec': metrics_at_99rec,
            'auroc': aurocs,
            'aupr': auprs,
        }
    
    def predict(self):
        predictions = self.model.predict(self.test_embeds)
        out_predictions = []
        for i in range(len(predictions)):
            class_i = np.argmax(predictions[i])
            out_predictions.append(self.classes[class_i])
        return out_predictions


class KMeansClassificationTask(BinaryClassificationTask):
    def __init__(self, test):
        (_, _, _, _, self.test_embeds) = self._load_data([], [], test)
        self.model = self._load_model()
    
    def _load_data(self, train, val, test):
        return super()._load_data(train, val, test)

    def _load_model(self):
        return cluster.KMeans(n_clusters=2, random_state=0, max_iter=1000)
    
    def train(self):
        self.model.fit(self.test_embeds)
    
    def evaluate(self):
        # KMeans task is default task when no train/val data is provided.
        # Thus, it should not have an evaluate function.
        pass
    
    def predict(self):
        return self.model.predict(self.test_embeds)


def classify(text_to_label, prelabeled_text=None, output_metrics=False):
    if isinstance(text_to_label, pd.DataFrame):
        assert 'text' in text_to_label.columns, 'Make sure the text column in your pandas DataFrame is named "text".'
        text_to_label = text_to_label.text.tolist()
    if isinstance(prelabeled_text, pd.DataFrame):
        assert 'text' in prelabeled_text.columns and 'label' in prelabeled_text.columns, \
            'Make sure the text column in your pandas DataFrame is named "text" and the label column is named "label"'
        prelabeled_text = list(zip(prelabeled_text.text.tolist(), prelabeled_text.label.tolist()))

    # Perform KMeans if no training data is given.
    if prelabeled_text is None:
        task = KMeansClassificationTask(text_to_label)
        task.train()
        return task.predict()
    # Train a classifier if training data is given.
    else:
        if len(prelabeled_text) < 3:
            raise ValueError('prelabeled_text has too few examples. At least 3 are required.')

        num_unique_classes = len(set([x[1] for x in prelabeled_text]))
        if num_unique_classes <= 1:
            raise ValueError('prelabeled_text contains examples from just one class. Examples from at least 2 classes are required.')
        elif num_unique_classes == 2:
            task = BinaryClassificationTask
        else:
            task = MulticlassClassificationTask

        classify_task_out = task(prelabeled_text, [], text_to_label)
        classify_task_out.train()
        results = classify_task_out.predict()

        # If output_metrics is also given, train a second time with a train val split.
        if output_metrics:
            split_attempt = 0
            metrics = None
            # Try 10 times to get a proper split. Sometimes, a split will cause all training examples to be
            # in the same class, which will error.
            while split_attempt < 10 and metrics is None:
                train, val = sklearn.model_selection.train_test_split(prelabeled_text, test_size=0.2)
                num_unique_classes_in_train = len(set([x[1] for x in train]))
                if num_unique_classes_in_train < 2:
                    split_attempt += 1
                    continue
                classify_task_metrics = task(train, val, text_to_label)
                classify_task_metrics.train()
                metrics = classify_task_metrics.evaluate()

            if metrics is None:
                print('''The provided prelabeled_text examples were not diverse enough to estimate performance.
                Try balancing your prelabeled_text examples by adding more examples of each class. Returning metrics
                as None.''')

    return (results, metrics) if output_metrics else results
