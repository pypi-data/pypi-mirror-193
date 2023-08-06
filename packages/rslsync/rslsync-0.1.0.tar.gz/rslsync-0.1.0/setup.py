# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rslsync', 'rslsync.commands']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'rslsync',
    'version': '0.1.0',
    'description': 'A Python client of unofficial Resilio Sync API',
    'long_description': 'None',
    'author': 'Zhongke Chen',
    'author_email': 'github@ch3n2k.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
