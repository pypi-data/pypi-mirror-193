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
    'version': '0.1.5',
    'description': 'GUET WiFi Monitor',
    'long_description': '# guetwifi\n\nThis is a simple script to connect to the GUET-WIFI and keep it alive!!!!!!.\n\n## Usage\n\n### Installation\n\n```bash\npip install guetwifi\n```\n\n### help\n\n```bash\nguetwifi --help\n```\n\n```bash\nUsage: guetwifi [OPTIONS] COMMAND [ARGS]...\n\n  GuetWifi is a command line tool for GUET-WIFI login\n\nOptions:\n  --debug / --no-debug\n  --help                Show this message and exit.\n\nCommands:\n  config   Config your GUET-WIFI account and password\n  log      Show guetwifi log\n  restart  Restart guetwifi\n  start    Start guetwifi\n  status   Check guetwifi status\n  stop     Stop guetwifi\n  version  Show guetwifi version\n```\n\n### config\n\n```bash\nguetwifi config --help\n```\n\n```bash\nguetwifi config -a <account> -p <password>\n```\n\nyou can set the isp to `cmcc` or `telecom` and `unicom` using `-i` option.\n\n```bash\nguetwifi config -a <account> -p <password> -i <isp>\n```\n\n### start\n\n```bash\nguetwifi start\n```\n\n### stop\n\n```bash\nguetwifi stop\n```\n\n### status\n\n```bash\nguetwifi status\n```\n\n### log\n\n```bash\nguetwifi log\n```\n',
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
