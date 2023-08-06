# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ss13_tools',
 'ss13_tools.auth',
 'ss13_tools.byond',
 'ss13_tools.centcom',
 'ss13_tools.log_downloader',
 'ss13_tools.scrubby',
 'ss13_tools.slur_detector']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.8.3,<4.0.0',
 'colorama>=0.4.6,<0.5.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'requests>=2.28.1,<3.0.0',
 'tqdm>=4.64.1,<5.0.0']

setup_kwargs = {
    'name': 'ss13-tools',
    'version': '2.0.0',
    'description': 'Python toolchain for SS13',
    'long_description': 'None',
    'author': 'RigglePrime',
    'author_email': '27156122+RigglePrime@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9.1,<3.12',
}


setup(**setup_kwargs)
