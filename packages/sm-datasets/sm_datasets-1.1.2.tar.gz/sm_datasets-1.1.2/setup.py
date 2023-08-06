# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sm_datasets', 'sm_datasets.migrations']

package_data = \
{'': ['*']}

install_requires = \
['kgdata>=3.4.2,<4.0.0',
 'loguru>=0.6.0,<0.7.0',
 'python-slugify>=6.1.2,<7.0.0',
 'rdflib>=6.1.1,<7.0.0',
 'rsoup>=2.5.1,<3.0.0',
 'sem-desc>=4.4.2,<5.0.0']

setup_kwargs = {
    'name': 'sm-datasets',
    'version': '1.1.2',
    'description': 'Datasets for benchmarking Semantic Modeling problem',
    'long_description': 'Datasets for the semantic modeling problem\n',
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
