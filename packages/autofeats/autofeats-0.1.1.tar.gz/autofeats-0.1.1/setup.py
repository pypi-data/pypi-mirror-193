# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autofeats', 'autofeats.features']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.5.3,<2.0.0', 'pyspark>=3.3.1,<4.0.0']

setup_kwargs = {
    'name': 'autofeats',
    'version': '0.1.1',
    'description': '',
    'long_description': None,
    'author': 'Felipe Sassi',
    'author_email': 'felipesassi@outlook.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/felipesassi/autofeats',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
