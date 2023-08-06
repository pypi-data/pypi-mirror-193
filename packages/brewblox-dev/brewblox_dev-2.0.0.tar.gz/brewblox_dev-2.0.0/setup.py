# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['brewblox_dev']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'flake8>5', 'python-dotenv>=0.21.1,<0.22.0']

entry_points = \
{'console_scripts': ['brewblox-dev = brewblox_dev.__main__:main']}

setup_kwargs = {
    'name': 'brewblox-dev',
    'version': '2.0.0',
    'description': 'Brewblox development tools',
    'long_description': 'None',
    'author': 'BrewPi',
    'author_email': 'development@brewpi.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
