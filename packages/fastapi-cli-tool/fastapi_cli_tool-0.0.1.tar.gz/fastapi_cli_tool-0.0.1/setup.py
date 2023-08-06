# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_cli_tool',
 'fastapi_cli_tool.template.app_name',
 'fastapi_cli_tool.template.app_name.api',
 'fastapi_cli_tool.template.app_name.crud',
 'fastapi_cli_tool.template.database',
 'fastapi_cli_tool.template.project_name',
 'fastapi_cli_tool.template.project_name.backend',
 'fastapi_cli_tool.template.project_name.core',
 'fastapi_cli_tool.template.project_name.core.conf',
 'fastapi_cli_tool.template.project_name.core.contrib',
 'fastapi_cli_tool.template.project_name.core.utils',
 'fastapi_cli_tool.template.project_name.tests']

package_data = \
{'': ['*']}

install_requires = \
['copier>=7.0.1,<8.0.0',
 'inquirerpy>=0.3.4,<0.4.0',
 'requests>=2.28.2,<3.0.0',
 'tomlkit>=0.11.6,<0.12.0',
 'typer[all]>=0.7.0,<0.8.0']

entry_points = \
{'console_scripts': ['fastapi-cli = fastapi_cli_tool.main:app']}

setup_kwargs = {
    'name': 'fastapi-cli-tool',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'christoph-xd',
    'author_email': 'cbsk.tech@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
