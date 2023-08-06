# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['smyg', 'smyg.metrics']

package_data = \
{'': ['*'], 'smyg': ['templates/*']}

setup_kwargs = {
    'name': 'smyg',
    'version': '0.3.2',
    'description': 'git metric calculation',
    'long_description': 'None',
    'author': 'Nikolay Mikhaylichenko',
    'author_email': 'nn.mikh@yandex.ru',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
}


setup(**setup_kwargs)
