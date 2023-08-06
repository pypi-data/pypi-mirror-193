# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pytest-pyspec']

package_data = \
{'': ['*']}

install_requires = \
['pytest>=7.2.1,<8.0.0']

entry_points = \
{'pytest11': ['pytest-pyspec = pytest-pyspec.plugin']}

setup_kwargs = {
    'name': 'pytest-pyspec',
    'version': '0.1.0',
    'description': 'A python test spec based on pytest',
    'long_description': '',
    'author': 'Felipe Curty',
    'author_email': 'felipecrp@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
