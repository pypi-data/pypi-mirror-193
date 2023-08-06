# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['natural_python']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.26.5,<0.27.0']

entry_points = \
{'console_scripts': ['natural-python = natural_python.console:main']}

setup_kwargs = {
    'name': 'natural-python',
    'version': '0.1.8',
    'description': '',
    'long_description': "# natural-python\n\n[Gitlab repository](https://gitlab.com/da_doomer/natural-python) | [Github mirror](https://github.com/dadoomer/natural-python) | [Blog post](https://iamleo.space/2023-02-20-llm-python-repl/)\n\nThis is a wrapper around the Python REPL which uses LLMs to search for code that matches your natural language specification and Python constraints.\n\nNaturally, from a safety perspective the output of an LLM can only be assumed to be adversarial. Indeed, executing the output of an LLM is an inherently dangerous approach to implementing a REPL. Use at your own peril.\n\n## Example\n\nHello world session: given this input\n\n```python\n>>> # Create a list with the days of the week, call it 'days'\n>>> # finally:\n+++ assert days[0] == 'Sunday'\n+++\n```\n\nthe interpreter will write the following code:\n\n```python\n>>> days = [\n>>>     'Sunday',\n>>>     'Monday',\n>>>     'Tuesday',\n>>>     'Wednesday',\n>>>     'Thursday',\n>>>     'Friday',\n>>>     'Saturday',\n>>> ]\n>>> assert days[0] == 'Sunday'\n```\n\n## Installation\n\n`pip install --user --upgrade git+https://gitlab.com/da_doomer/natural-python.git`\n\n(You can remove `--upgrade` if your pip is reasonably updated)\n\nThen simply execute `natural-python --output my_script.py` in your shell (`--output` is an optional parameter).\n\nThe first time the interpreter is executed, it will ask for an API key. Currently, the interpreter supports GooseAI and OpenAI endpoints.\n\n## Usage\n\nRun `natural-python --help` to get the following:\n\n```\nusage: natural-python [-h] [--engine-id ENGINE_ID] [--sample-n SAMPLE_N] [--sample-temperature SAMPLE_TEMPERATURE] [--max-sample-tokens MAX_SAMPLE_TOKENS]\n                      [--python-shell PYTHON_SHELL] [--show-engines] [--output OUTPUT]\n\nNatural Python interpreter.\n\noptions:\n  -h, --help            show this help message and exit\n  --engine-id ENGINE_ID\n                        Language model engine used for sampling.\n  --sample-n SAMPLE_N   Number of samples drawn from the language model when executing an instruction.\n  --sample-temperature SAMPLE_TEMPERATURE\n                        Sampling temperature.\n  --max-sample-tokens MAX_SAMPLE_TOKENS\n                        Maximum number of tokens in each sample.\n  --python-shell PYTHON_SHELL\n                        Engine used for sampling.\n  --show-engines        Display available language model engines.\n  --output OUTPUT       Write the source code to a file at the end of the session.\n```\n",
    'author': 'Leo',
    'author_email': 'leohdz.c0@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
