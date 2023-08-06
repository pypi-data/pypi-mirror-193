# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aiogram_fastapi_server']

package_data = \
{'': ['*']}

install_requires = \
['aiogram>=3.0.0b1,<4.0.0', 'fastapi']

setup_kwargs = {
    'name': 'aiogram-fastapi-server',
    'version': '0.1.1',
    'description': 'Handle webhook requests with FastAPI instead of aiohttp',
    'long_description': '# Aiogram FastAPI Server\nHandle webhook requests with FastAPI instead of aiohttp  \nBased on https://github.com/aiogram/aiogram/blob/dev-3.x/aiogram/webhook/aiohttp_server.py  \n\n# Check out our aiogram bot template\nhttps://github.com/4u-org/bot-template\n',
    'author': 'Snimshchikov Ilya',
    'author_email': 'snimshchikov.ilya@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
