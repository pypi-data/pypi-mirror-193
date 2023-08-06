# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py3html']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'py3html',
    'version': '0.1.4',
    'description': 'A very simple tool to generate html with python code.',
    'long_description': 'None',
    'author': 'Ozcan Yarimdunya',
    'author_email': 'ozcanyd@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
