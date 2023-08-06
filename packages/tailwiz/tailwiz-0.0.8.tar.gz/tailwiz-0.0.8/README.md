# Text Labeling AI Wizard (tailwiz)

`tailwiz` is an AI-powered tool for labeling text. It has three main capabilties: classifying text (`tailwiz.classify`), parsing text given context and prompts (`tailwiz.parse`), and generating text given prompts (`tailwiz.generate`).

## Installation

Install `tailwiz` through `pip`:

```
python -m pip install tailwiz
```

## Usage

In this section, we outline the three main functions of `tailwiz` and provide examples.


### <code>tailwiz.classify<i>(text_to_label, prelabeled_text=None, output_metrics=False)</i></code>

Given text, classify the text.
#### Parameters:
- `text_to_label` : _pandas.DataFrame_. Data structure containing text to classify. Must contain a string column named `text`.
- `prelabeled_text` : _pandas.DataFrame, default None_. Pre-labeled text to enhance the performance of the classification task. Must contain a string column for the classified text named `text` and a column for the labels named `label`.
- `output_metrics` : _bool, default False_. Whether to output `performance_estimate` together with results in a tuple.

#### Returns:
- `results` : _pandas.DataFrame_. A copy of `text_to_label` with a new column, `label_from_tailwiz`, containing classification results.
- `performance_estimate` : _Dict[str, float]_. Dictionary of metric name to metric value mappings. Included together with results in a tuple if `output_metrics` is True. Uses prelabeled_text to give an estimate of the accuracy of the classification. One vs. all metrics are given for multiclass classification.

#### Example:

```
>>> import tailwiz
>>> results = tailwiz.classify(
...     text_to_label=pd.DataFrame(['You are the best!', 'You make me sick'], columns=['text']),
...     prelabeled_text=pd.DataFrame([
...         ['Love you to the moon', 'nice'],
...         ['I hate you', 'mean'],
...         ['Have a great day', 'nice']
...     ], column=['text', 'label'])
... )
>>> results.label_from_tailwiz.tolist()
['nice', 'mean']
```

### <code>tailwiz.parse<i>(text_to_label, prelabeled_text=None, output_metrics=False)</i></code>

Given a prompt and a context, parse the answer from the context.
#### Parameters:
- `text_to_label` : _pandas.DataFrame_. Data containing prompts and contexts from which answers will be parsed. Must contain a string column for the context named `context` and a string column for the prompt named `prompt`.
- `prelabeled_text` : _pandas.DataFrame, default None_. Pre-labeled text to enhance the performance of the parsing task. Must contain a string column for the context named `context`, a string column for the prompt named `prompt`, and a string column for the label named `label`.
- `output_metrics` : _bool, default False_. Whether to output `performance_estimate` together with results in a tuple.

#### Returns:
- `results` : _pandas.DataFrame_. A copy of `text_to_label` with a new column, `label_from_tailwiz`, containing parsed results.
- `performance_estimate` : _Dict[str, float]_. Dictionary of metric name to metric value mappings. Included together with results in a tuple if `output_metrics` is True. Uses prelabeled_text to give an estimate of the accuracy of the parsing job.

#### Example:
```
>>> import tailwiz
>>> results = tailwiz.parse(
...     text_to_label=pd.DataFrame([['Extract the number.', 'Figure 8']], columns=['prompt', 'context']),
...     prelabeled_text=pd.DataFrame([
...         ['Extract the number.', 'Noon is twelve oclock', 'twelve'],
...         ['Extract the number.', '10 jumping jacks', '10'],
...         ['Extract the number.', 'I have 3 eggs', '3'],
...     ], columns=['prompt', 'context', 'label'])
... )
>>> results.label_from_tailwiz.tolist()
['8']
```


### <code>tailwiz.generate<i>(text_to_label, prelabeled_text=None, output_metrics=False)</i></code>

Given a prompt, generate an answer.
#### Parameters:
- `text_to_label` : _pandas.DataFrame_. Data structure containing prompts for which answers will be generated. Must contain a string column for the prompt named `prompt`.
- `prelabeled_text` : _pandas.DataFrame, default None_. Pre-labeled text to enhance the performance of the text generation task. Must contain a string column for the prompt named `prompt` and a string column for the label named `label`.
- `output_metrics` : _bool, default False_. Whether to output `performance_estimate` together with results in a tuple.

#### Returns:
- `results` : _pandas.DataFrame_. A copy of `text_to_label` with a new column, `label_from_tailwiz`, containing generated results.
- `performance_estimate` : _Dict[str, float]_. Dictionary of metric name to metric value mappings. Included together with results in a tuple if `output_metrics` is True. Uses prelabeled_text to give an estimate of the accuracy of the text generation job.

#### Example:
```
>>> import tailwiz
>>> results = tailwiz.generate(
...     text_to_label=pd.DataFrame(['Is this sentence Happy or Sad? I am crying my eyes out.'], columns=['prompt']),
...     prelabeled_text=pd.DataFrame([
...         ['Is this sentence Happy or Sad? I love puppies!', 'Happy'],
...         ['Is this sentence Happy or Sad? I do not like you at all.', 'Sad'],
...     ], columns=['prompt', 'label'])
... )
>>> results.label_from_tailwiz.tolist()
['Sad']
```

## Templates (Notebooks)

Use these Jupyter Notebook examples as templates to help load your data and run any of the three `tailwiz` functions:
- For an example of `tailwiz.classify`, see [`examples/classify.ipynb`](https://github.com/timothydai/tailwiz/blob/main/examples/classify.ipynb)
- For an example of `tailwiz.parse`, see [`examples/parse.ipynb`](https://github.com/timothydai/tailwiz/blob/main/examples/parse.ipynb)
- For an example of `tailwiz.generate`, see [`examples/generate.ipynb`](https://github.com/timothydai/tailwiz/blob/main/examples/generate.ipynb)
