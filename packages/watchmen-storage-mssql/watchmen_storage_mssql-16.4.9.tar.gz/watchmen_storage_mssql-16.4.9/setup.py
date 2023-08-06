# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_storage_mssql']

package_data = \
{'': ['*']}

install_requires = \
['pyodbc>=4.0.32,<5.0.0', 'watchmen-storage-rds==16.4.9']

setup_kwargs = {
    'name': 'watchmen-storage-mssql',
    'version': '16.4.9',
    'description': '',
    'long_description': 'None',
    'author': 'botlikes',
    'author_email': '75356972+botlikes456@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
