# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['spacesay']

package_data = \
{'': ['*']}

install_requires = \
['pyyaml>=6.0,<7.0', 'requests>=2.28.2,<3.0.0', 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['spacesay = spacesay.main:app']}

setup_kwargs = {
    'name': 'spacesay',
    'version': '0.1.1',
    'description': 'A CLI spaceman tells you where the ISS is!',
    'long_description': '# Spacesay\n\nA python reimagining of cowsay.\n\nHave a astronaut say something, or let it tell you where the ISS is currently!\n\n',
    'author': 'AlgorithmEnigma',
    'author_email': 'me@jordanlowell.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
