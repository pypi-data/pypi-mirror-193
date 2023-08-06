# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['learning_machines_drift']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.2,<4.0.0',
 'numpy>=1.22.4,<2.0.0',
 'pandas>=1.5,<2.0',
 'pydantic>=1.9.1,<2.0.0',
 'pygments>=2.11.2,<3.0.0',
 'scipy>=1.8.1,<2.0.0',
 'sdmetrics==0.8.0',
 'tabulate>=0.8.10,<0.9.0']

setup_kwargs = {
    'name': 'learning-machines-drift',
    'version': '0.0.3',
    'description': 'A Python package for monitoring dataset drift in secure environments.',
    'long_description': 'None',
    'author': 'Sam Greenbury',
    'author_email': 'sgreenbury@turing.ac.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)
