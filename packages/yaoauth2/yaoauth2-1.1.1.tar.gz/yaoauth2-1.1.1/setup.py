# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yaoauth2', 'yaoauth2.providers']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.92,<0.93', 'httpx>=0.23,<0.24', 'nxtools>=1.6,<2.0']

setup_kwargs = {
    'name': 'yaoauth2',
    'version': '1.1.1',
    'description': 'Simple OAuth2 client library for FastAPI',
    'long_description': None,
    'author': 'Martin Wacker',
    'author_email': 'martas@imm.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
