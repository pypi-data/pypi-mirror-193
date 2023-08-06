# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['alexandra_ai']

package_data = \
{'': ['*']}

install_requires = \
['alexandra-ai-eval>=0.1.0,<0.2.0']

setup_kwargs = {
    'name': 'alexandra-ai',
    'version': '0.1.0',
    'description': 'Alexandra Institute Artificial Intelligence, a Python package for Danish data science.',
    'long_description': '# AlexandraAI\n\n### A Python package for Danish data science\n\n______________________________________________________________________\n[![PyPI Status](https://badge.fury.io/py/alexandra_ai.svg)](https://pypi.org/project/alexandra_ai/)\n[![Documentation](https://img.shields.io/badge/docs-passing-green)](https://alexandrainst.github.io/AlexandraAI/alexandra_ai.html)\n[![License](https://img.shields.io/github/license/alexandrainst/AlexandraAI)](https://github.com/alexandrainst/AlexandraAI/blob/main/LICENSE)\n[![LastCommit](https://img.shields.io/github/last-commit/alexandrainst/AlexandraAI)](https://github.com/alexandrainst/AlexandraAI/commits/main)\n[![Code Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](https://github.com/alexandrainst/AlexandraAI/tree/main/tests)\n\n## Installation\n\nTo install the package simply write the following command in your favorite terminal:\n\n```\npip install alexandra-ai\n```\n\n## Quickstart\n\n### Benchmarking from the Command Line\n\nThe easiest way to benchmark pretrained models is via the command line interface. After\nhaving installed the package, you can benchmark your favorite model like so:\n\n```\nevaluate --model-id <model_id> --task <task>\n```\n\nHere `model_id` is the HuggingFace model ID, which can be found on the [HuggingFace\nHub](https://huggingface.co/models), and `task` is the task you want to benchmark the\nmodel on, such as "ner" for named entity recognition. See all options by typing\n\n```\nevaluate --help\n```\n\nThe specific model version to use can also be added after the suffix \'@\':\n\n```\nevaluate --model_id <model_id>@<commit>\n```\n\nIt can be a branch name, a tag name, or a commit id. It defaults to \'main\' for latest.\n\nMultiple models and tasks can be specified by just attaching multiple arguments. Here\nis an example with two models:\n\n```\nevaluate --model_id <model_id1> --model_id <model_id2> --task ner\n```\n\nSee all the arguments and options available for the `evaluate` command by typing\n\n```\nevaluate --help\n```\n\n### Benchmarking from a Script\n\nIn a script, the syntax is similar to the command line interface. You simply initialise\nan object of the `Evaluator` class, and call this evaluate object with your favorite\nmodels and/or datasets:\n\n```\n>>> from alexandra_ai import Evaluator\n>>> evaluator = Evaluator()\n>>> evaluator(\'<model_id>\', \'<task>\')\n```\n\n## Contributors\n\nIf you feel like this package is missing a crucial feature, if you encounter a bug or\nif you just want to correct a typo in this readme file, then we urge you to join the\ncommunity! Have a look at the [CONTRIBUTING.md](./CONTRIBUTING.md) file, where you can\ncheck out all the ways you can contribute to this package. :sparkles:\n\n- _Your name here?_ :tada:\n\n## Maintainers\n\nThe following are the core maintainers of the `alexandra_ai` package:\n\n- [@saattrupdan](https://github.com/saattrupdan) (Dan Saattrup Nielsen; saattrupdan@alexandra.dk)\n- [@AJDERS](https://github.com/AJDERS) (Anders Jess Pedersen; anders.j.pedersen@alexandra.dk)\n\n## The AlexandraAI ecosystem\n\nThis package is a wrapper around other AlexandraAI packages, each of which is standalone:\n\n- [AlexandraAI-eval](https://github.com/alexandrainst/AlexandraAI-eval): Evaluation of finetuned models.\n\n## Project structure\n\n```\n.\n├── .flake8\n├── .github\n│\xa0\xa0 └── workflows\n│\xa0\xa0     ├── ci.yaml\n│\xa0\xa0     └── docs.yaml\n├── .gitignore\n├── .pre-commit-config.yaml\n├── CHANGELOG.md\n├── CODE_OF_CONDUCT.md\n├── CONTRIBUTING.md\n├── LICENSE\n├── README.md\n├── gfx\n├── makefile\n├── notebooks\n├── poetry.toml\n├── pyproject.toml\n├── src\n│\xa0\xa0 ├── alexandra_ai\n│\xa0\xa0 │\xa0\xa0 └── __init__.py\n│\xa0\xa0 └── scripts\n│\xa0\xa0     ├── fix_dot_env_file.py\n│\xa0\xa0     └── versioning.py\n└── tests\n    └── __init__.py\n```\n',
    'author': 'Dan Saattrup Nielsen',
    'author_email': 'dan.nielsen@alexandra.dk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
