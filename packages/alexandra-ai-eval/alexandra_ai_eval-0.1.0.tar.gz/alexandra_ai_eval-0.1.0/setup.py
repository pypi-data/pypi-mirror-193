# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['alexandra_ai_eval']

package_data = \
{'': ['*']}

install_requires = \
['codecarbon>=2.1.3,<3.0.0',
 'colorama>=0.4.5,<1.0.0',
 'datasets>=2.4.0,<3.0.0',
 'evaluate>=0.3.0,<1.0.0',
 'fsspec>=2022.7.1,<2023.0.0',
 'gradio>=3.1.7,<4.0.0',
 'huggingface-hub>=0.8.1,<1.0.0',
 'jiwer>=2.5.1,<3.0.0',
 'librosa>=0.9.2,<1.0.0',
 'protobuf>=3.0.0,<3.21.0',
 'psutil>=5.9.0,<5.9.2',
 'pyctcdecode>=0.4.0,<1.0.0',
 'pypi-kenlm>=0.1.20220713,<1.0.0',
 'sentencepiece>=0.1.96,<1.0.0',
 'seqeval>=1.2.2,<2.0.0',
 'soundfile>=0.11.0,<1.0.0',
 'spacy>=3.4.1,<4.0.0',
 'tabulate>=0.9.0,<1.0.0',
 'termcolor>=1.1.0,<2.0.0',
 'torch>=1.13.1,<2.0.0',
 'torchaudio>=0.13.1,<1.0.0',
 'tqdm>=4.64.0,<5.0.0',
 'transformers>=4.23.0,<5.0.0']

entry_points = \
{'console_scripts': ['evaluate = alexandra_ai_eval.cli:evaluate',
                     'evaluate-gui = alexandra_ai_eval.gui:main']}

setup_kwargs = {
    'name': 'alexandra-ai-eval',
    'version': '0.1.0',
    'description': 'Evaluation of finetuned models.',
    'long_description': '# AlexandraAI-eval\n\n### Evaluation of finetuned models\n\n##### _(pronounced as in "Aye aye captain")_\n\n______________________________________________________________________\n[![PyPI Status](https://badge.fury.io/py/alexandra_ai_eval.svg)](https://pypi.org/project/alexandra_ai_eval/)\n[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://alexandrainst.github.io/AlexandraAI-eval/alexandra_ai_eval.html)\n[![License](https://img.shields.io/github/license/alexandrainst/AlexandraAI-eval)](https://github.com/alexandrainst/AlexandraAI-eval/blob/main/LICENSE)\n[![LastCommit](https://img.shields.io/github/last-commit/alexandrainst/AlexandraAI-eval)](https://github.com/alexandrainst/AlexandraAI-eval/commits/main)\n[![Code Coverage](https://img.shields.io/badge/Coverage-78%25-yellowgreen.svg)](https://github.com/alexandrainst/AlexandraAI-eval/tree/main/tests)\n\n## Installation\n\nTo install the package simply write the following command in your favorite terminal:\n\n```\npip install alexandra-ai-eval\n```\n\n## Quickstart\n\n### Benchmarking from the Command Line\n\nThe easiest way to benchmark pretrained models is via the command line interface. After\nhaving installed the package, you can benchmark your favorite model like so:\n\n```\nevaluate --model-id <model_id> --task <task>\n```\n\nHere `model_id` is the HuggingFace model ID, which can be found on the [HuggingFace\nHub](https://huggingface.co/models), and `task` is the task you want to benchmark the\nmodel on, such as "ner" for named entity recognition. See all options by typing\n\n```\nevaluate --help\n```\n\nThe specific model version to use can also be added after the suffix \'@\':\n\n```\nevaluate --model_id <model_id>@<commit>\n```\n\nIt can be a branch name, a tag name, or a commit id. It defaults to \'main\' for latest.\n\nMultiple models and tasks can be specified by just attaching multiple arguments. Here\nis an example with two models:\n\n```\nevaluate --model_id <model_id1> --model_id <model_id2> --task ner\n```\n\nSee all the arguments and options available for the `evaluate` command by typing\n\n```\nevaluate --help\n```\n\n### Benchmarking from a Script\n\nIn a script, the syntax is similar to the command line interface. You simply initialise\nan object of the `Evaluator` class, and call this evaluate object with your favorite\nmodels and/or datasets:\n\n```\n>>> from alexandra_ai_eval import Evaluator\n>>> evaluator = Evaluator()\n>>> evaluator(\'<model_id>\', \'<task>\')\n```\n\n## Contributors\n\nIf you feel like this package is missing a crucial feature, if you encounter a bug or\nif you just want to correct a typo in this readme file, then we urge you to join the\ncommunity! Have a look at the [CONTRIBUTING.md](./CONTRIBUTING.md) file, where you can\ncheck out all the ways you can contribute to this package. :sparkles:\n\n- _Your name here?_ :tada:\n\n## Maintainers\n\nThe following are the core maintainers of the `alexandra_ai_eval` package:\n\n- [@saattrupdan](https://github.com/saattrupdan) (Dan Saattrup Nielsen; saattrupdan@alexandra.dk)\n- [@AJDERS](https://github.com/AJDERS) (Anders Jess Pedersen; anders.j.pedersen@alexandra.dk)\n\n## Project structure\n\n```\n.\n├── .flake8\n├── .github\n│\xa0\xa0 └── workflows\n│\xa0\xa0     ├── ci.yaml\n│\xa0\xa0     └── docs.yaml\n├── .gitignore\n├── .pre-commit-config.yaml\n├── LICENSE\n├── README.md\n├── gfx\n│\xa0\xa0 └── alexandra-ai-eval-logo.png\n├── makefile\n├── models\n├── notebooks\n├── poetry.toml\n├── pyproject.toml\n├── src\n│\xa0\xa0 ├── alexandra_ai_eval\n│\xa0\xa0 │\xa0\xa0 ├── __init__.py\n│\xa0\xa0 │\xa0\xa0 ├── automatic_speech_recognition.py\n│\xa0\xa0 │\xa0\xa0 ├── cli.py\n│\xa0\xa0 │\xa0\xa0 ├── co2.py\n│\xa0\xa0 │\xa0\xa0 ├── config.py\n│\xa0\xa0 │\xa0\xa0 ├── country_codes.py\n│\xa0\xa0 │\xa0\xa0 ├── evaluator.py\n│\xa0\xa0 │\xa0\xa0 ├── exceptions.py\n│\xa0\xa0 │\xa0\xa0 ├── hf_hub.py\n│\xa0\xa0 │\xa0\xa0 ├── image_to_text.py\n│\xa0\xa0 │\xa0\xa0 ├── named_entity_recognition.py\n│\xa0\xa0 │\xa0\xa0 ├── question_answering.py\n│\xa0\xa0 │\xa0\xa0 ├── scoring.py\n│\xa0\xa0 │\xa0\xa0 ├── task.py\n│\xa0\xa0 │\xa0\xa0 ├── task_configs.py\n│\xa0\xa0 │\xa0\xa0 ├── task_factory.py\n│\xa0\xa0 │\xa0\xa0 ├── text_classification.py\n│\xa0\xa0 │\xa0\xa0 └── utils.py\n│\xa0\xa0 └── scripts\n│\xa0\xa0     ├── fix_dot_env_file.py\n│\xa0\xa0     └── versioning.py\n└── tests\n    ├── __init__.py\n    ├── conftest.py\n    ├── test_cli.py\n    ├── test_co2.py\n    ├── test_config.py\n    ├── test_country_codes.py\n    ├── test_evaluator.py\n    ├── test_exceptions.py\n    ├── test_hf_hub.py\n    ├── test_image_to_text.py\n    ├── test_named_entity_recognition.py\n    ├── test_question_answering.py\n    ├── test_scoring.py\n    ├── test_task.py\n    ├── test_task_configs.py\n    ├── test_task_factory.py\n    ├── test_text_classification.py\n    └── test_utils.py\n```\n',
    'author': 'Dan Saattrup Nielsen',
    'author_email': 'dan.nielsen@alexandra.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
