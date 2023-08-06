# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stablerandom']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0']

setup_kwargs = {
    'name': 'stablerandom',
    'version': '0.2.21',
    'description': 'Create stable/repeatable numpy.random applications',
    'long_description': 'None',
    'author': 'John Heintz',
    'author_email': 'john@gistlabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
