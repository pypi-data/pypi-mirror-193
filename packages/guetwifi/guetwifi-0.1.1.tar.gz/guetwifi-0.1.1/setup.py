# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['guetwifi']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.0,<9.0.0', 'psutil>=5.7.2,<6.0.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['guetwifi = guetwifi.cli:main']}

setup_kwargs = {
    'name': 'guetwifi',
    'version': '0.1.1',
    'description': 'GUET WiFi Monitor',
    'long_description': '## GUET-WIFI Auto Login\n\n### Usage\n\n#### Linux\n\nFirst, install the package:\n\n```bash\npip install guetwifi\n```\n\nThen, run the command in terminal:\n\n```bash\nguetwifi start\n```\n\n#### Windows\n\n> Please use the Windows Subsystem for Linux (WSL) to run this program.',
    'author': 'PuQing',
    'author_email': 'me@puqing.work',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/andPuQing/guetwifi',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
