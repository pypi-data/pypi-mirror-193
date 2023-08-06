# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['devtools',
 'devtools.exceptions',
 'devtools.models',
 'devtools.providers',
 'devtools.providers.database',
 'devtools.providers.database.filters',
 'devtools.providers.database.helpers',
 'devtools.providers.database.types',
 'devtools.tests',
 'devtools.types',
 'devtools.utils']

package_data = \
{'': ['*']}

install_requires = \
['aioredis>=2.0.1,<3.0.0',
 'aiosqlite>=0.18.0,<0.19.0',
 'asyncpg>=0.27.0,<0.28.0',
 'cffi>=1.15.1,<2.0.0',
 'faker>=17.0.0,<18.0.0',
 'fakeredis>=2.9.2,<3.0.0',
 'fastapi>=0.92.0,<0.93.0',
 'httpx>=0.23.3,<0.24.0',
 'orjson>=3.8.6,<4.0.0',
 'pycryptodome>=3.17,<4.0',
 'pydantic>=1.10.4,<2.0.0',
 'pytest-asyncio>=0.20.3,<0.21.0',
 'pytest>=7.2.1,<8.0.0',
 'requests>=2.28.2,<3.0.0',
 'sqlalchemy>=2.0.4,<3.0.0',
 'starlette>=0.25.0,<0.26.0']

setup_kwargs = {
    'name': 'eric-devtools',
    'version': '0.3.0',
    'description': '',
    'long_description': '',
    'author': 'Eric Batista',
    'author_email': 'klose.eric31@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
