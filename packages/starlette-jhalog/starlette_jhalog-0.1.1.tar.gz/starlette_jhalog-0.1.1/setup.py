# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['starlette_jhalog']

package_data = \
{'': ['*']}

install_requires = \
['jhalog', 'starlette']

setup_kwargs = {
    'name': 'starlette-jhalog',
    'version': '0.1.1',
    'description': 'Jhalog (JSON HTTP Access Log) middleware for Starlette/FastAPI',
    'long_description': '![Tests](https://github.com/JGoutin/starlette-jhalog/workflows/tests/badge.svg)\n[![codecov](https://codecov.io/gh/JGoutin/starlette-jhalog/branch/main/graph/badge.svg)](https://codecov.io/gh/JGoutin/starlette-jhalog)\n[![PyPI](https://img.shields.io/pypi/v/starlette-jhalog.svg)](https://pypi.org/project/starlette-jhalog)\n\n# Jhalog (JSON HTTP Access Log) - Starlette/FastAPI middleware\n\nStarlette/FastAPI middleware to use Jhalog as access log.\n\n[Jhalog Specification](https://github.com/JGoutin/jhalog-spec)\n\nWIP\n',
    'author': 'JGoutin',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/JGoutin/starlette-jhalog',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
