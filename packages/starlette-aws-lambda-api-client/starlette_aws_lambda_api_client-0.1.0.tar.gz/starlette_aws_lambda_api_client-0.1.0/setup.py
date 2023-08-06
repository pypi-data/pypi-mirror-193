# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlette_aws_lambda_api_client']

package_data = \
{'': ['*']}

install_requires = \
['aioboto3', 'jhalog', 'starlette']

extras_require = \
{'speedups': ['aiohttp[speedups]>3.8', 'orjson']}

setup_kwargs = {
    'name': 'starlette-aws-lambda-api-client',
    'version': '0.1.0',
    'description': 'aio_lambda_api with AWS lambda backend client for Starlette/FastAPI',
    'long_description': '![Tests](https://github.com/JGoutin/starlette_aws_lambda_api_client/workflows/tests/badge.svg)\n[![codecov](https://codecov.io/gh/JGoutin/starlette_aws_lambda_api_client/branch/main/graph/badge.svg)](https://codecov.io/gh/JGoutin/starlette_aws_lambda_api_client)\n[![PyPI](https://img.shields.io/pypi/v/starlette_aws_lambda_api_client.svg)](https://pypi.org/project/starlette_aws_lambda_api_client)\n\nWIP\n',
    'author': 'JGoutin',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JGoutin/starlette_aws_lambda_api_client',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
