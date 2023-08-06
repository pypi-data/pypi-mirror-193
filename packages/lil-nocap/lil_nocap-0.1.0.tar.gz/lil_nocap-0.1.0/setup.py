# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lil_nocap']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0', 'pandas>=1.5.3,<2.0.0']

setup_kwargs = {
    'name': 'lil-nocap',
    'version': '0.1.0',
    'description': 'A package for downloading bulk files from courtlistener',
    'long_description': '',
    'author': 'sabzo',
    'author_email': 'sabelo@sabelo.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
