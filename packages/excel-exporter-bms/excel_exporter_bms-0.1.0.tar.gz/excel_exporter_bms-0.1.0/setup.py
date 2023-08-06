# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['excel_exporter',
 'excel_exporter.configuration',
 'excel_exporter.exporter',
 'excel_exporter.utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0,<7.0', 'openpyxl>=3.1.1,<4.0.0']

entry_points = \
{'console_scripts': ['example = example:example']}

setup_kwargs = {
    'name': 'excel-exporter-bms',
    'version': '0.1.0',
    'description': 'A excel exporter based on YAML configuration files',
    'long_description': 'None',
    'author': 'Bruno Santiago',
    'author_email': 'brunomsantiago@gmail.com',
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
