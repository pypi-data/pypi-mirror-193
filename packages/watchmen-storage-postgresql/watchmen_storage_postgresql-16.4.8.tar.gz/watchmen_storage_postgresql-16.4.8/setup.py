# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_storage_postgresql']

package_data = \
{'': ['*']}

install_requires = \
['psycopg2-binary>=2.9.3,<3.0.0', 'watchmen-storage-rds==16.4.8']

setup_kwargs = {
    'name': 'watchmen-storage-postgresql',
    'version': '16.4.8',
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
