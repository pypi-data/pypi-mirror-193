# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyProjExample']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0', 'pre-commit>=3.1.0,<4.0.0', 'pytest>=7.2.1,<8.0.0']

setup_kwargs = {
    'name': 'pyprojexample',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Richard Bell',
    'author_email': 'rcbell@eng.ucsd.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
