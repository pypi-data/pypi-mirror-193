# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'python'}

packages = \
['rombus', 'rombus.scripts', 'rombus.tests', 'rombus.tests.resources']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'matplotlib>=3.6.2,<4.0.0',
 'mpi4py>=3.1.4,<4.0.0',
 'scipy>=1.9.3,<2.0.0',
 'six>=1.16.0,<2.0.0',
 'tqdm>=4.64.1,<5.0.0']

extras_require = \
{'dev': ['pre-commit>=3.0.4,<4.0.0',
         'pytest>=7.0,<8.0',
         'black>=22.10.0,<23.0.0',
         'ruff>=0.0.243,<0.0.244'],
 'docs': ['Sphinx==5.3.0',
          'sphinx-rtd-theme==1.0.0',
          'myst-parser>=0.18.1,<0.19.0']}

entry_points = \
{'console_scripts': ['rombus = rombus.scripts.cli:cli']}

setup_kwargs = {
    'name': 'rombus',
    'version': '0.1.18',
    'description': 'Reduced order modeling for the masses',
    'long_description': 'Rombus\n======\n\nThis project is being developed in the course of delivering the RSmith_2022B ADACS Merit Allocation Program project.\n',
    'author': 'Gregory Poole',
    'author_email': 'gbpoole@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/ADACS-Australia/rombus',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.11',
}


setup(**setup_kwargs)
