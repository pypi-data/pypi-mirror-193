# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyjuggler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyjuggler',
    'version': '0.1.0',
    'description': 'Multi-processing for Python',
    'long_description': '# pyjuggler\n\nMulti-processing for Python simplified',
    'author': 'chinmay',
    'author_email': 'hi@chinmayshah.xyz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
