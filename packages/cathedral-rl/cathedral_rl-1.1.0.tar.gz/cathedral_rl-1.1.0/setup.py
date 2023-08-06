# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cathedral_rl', 'cathedral_rl.examples', 'cathedral_rl.game']

package_data = \
{'': ['*']}

install_requires = \
['PettingZoo>=1.22.3,<2.0.0',
 'SuperSuit>=3.7.1,<4.0.0',
 'gymnasium>=0.27.1,<0.28.0',
 'numpy==1.22.0',
 'poetry>=1.3.2,<2.0.0',
 'pygame>=2.1.3,<3.0.0']

setup_kwargs = {
    'name': 'cathedral-rl',
    'version': '1.1.0',
    'description': 'Interactive Multi-Agent Reinforcement Learning Environment for the board game Cathedral using PettingZoo',
    'long_description': '[![PyPI version](https://badge.fury.io/py/cathedral-rl.svg?branch=master&kill_cache=1)](https://badge.fury.io/py/cathedral-rl)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![License](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://github.com/elliottower/cathedral-rl/blob/main/LICENSE)\n\n# cathedral-rl\nInteractive Multi-Agent Reinforcement Learning Environment for the board game Cathedral using PettingZoo\n',
    'author': 'elliottower',
    'author_email': 'elliot@elliottower.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/elliottower/cathedral-rl',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.12',
}


setup(**setup_kwargs)
