# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['weevils_cli']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0', 'tabulate>=0.8.10,<0.9.0']

entry_points = \
{'console_scripts': ['weevil = weevils_cli.entrypoint:cli',
                     'weevils = weevils_cli.entrypoint:cli']}

setup_kwargs = {
    'name': 'weevils-cli',
    'version': '0.0.2a1',
    'description': '',
    'long_description': 'None',
    'author': 'weevils.io',
    'author_email': 'code@weevils.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://docs.weevils.io/cli',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
