# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['origami', 'origami.defs', 'origami.tests', 'origami.tests.defs']

package_data = \
{'': ['*']}

install_requires = \
['backoff>=2.1.2,<3.0.0',
 'bitmath>=1.3.3,<2.0.0',
 'httpx>=0.23.0,<0.24.0',
 'jwt>=1.3.1,<2.0.0',
 'nbformat>=5.4.0,<6.0.0',
 'orjson>=3.6.8,<4.0.0',
 'pydantic>=1.9.0,<2.0.0',
 'structlog>=22.1.0,<23.0.0',
 'websockets>=10.3,<11.0']

setup_kwargs = {
    'name': 'noteable-origami',
    'version': '0.0.19',
    'description': 'The Noteable API interface',
    'long_description': '# Origami\nA library capturing message patterns and protocols speaking to Noteable\'s APIs\n<p align="center">\n<a href="https://github.com/noteable-io/origami/actions/workflows/ci.yaml">\n    <img src="https://github.com/noteable-io/origami/actions/workflows/ci.yaml/badge.svg" alt="CI" />\n</a>\n<a href="https://codecov.io/gh/noteable-io/origami" > \n <img src="https://codecov.io/gh/noteable-io/origami/branch/main/graph/badge.svg" alt="codecov code coverage"/> \n </a>\n<img alt="PyPI - License" src="https://img.shields.io/pypi/l/noteable-origami" />\n<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/noteable-origami" />\n<img alt="PyPI" src="https://img.shields.io/pypi/v/noteable-origami">\n<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>\n</p>\n\n---------\n\n[Install](#installation) | [Getting Started](#getting-started) | [License](./LICENSE) | [Code of Conduct](./CODE_OF_CONDUCT.md) | [Contributing](./CONTRIBUTING.md)\n\n<!-- --8<-- [start:intro] -->\n## Intro to Origami\n\nOrigami is our paper folding library for talking to [Noteable notebooks](http://noteable.io/). This is where we describe the full breadth of API calls and access patterns in async Python for rich programmatic access to the platform. You can use the platform for free with a quick signup.\n<!-- --8<-- [end:intro] -->\n\n<!-- --8<-- [start:requirements] -->\n## Requirements\n\nPython 3.8+\n<!-- --8<-- [end:requirements] -->\n\n<!-- --8<-- [start:install] -->\n## Installation\n\n### Poetry\n\n```shell\npoetry add noteable-origami\n```\n\n\n### Pip\n```shell\npip install noteable-origami\n```\n<!-- --8<-- [end:install] -->\n\n<!-- --8<-- [start:start] -->\n## Getting Started\n\nGet your API token from Noteable Within user settings.\nWithin user settings, go to the API Token page, and generate a new token. \n\nCopy the value\n\n```python\nfrom origami.client import NoteableClient\n\ntoken = \'ey...\' # Your user API token\nasync with NoteableClient(api_token=token) as client:\n    await client.ping_rtu()\n```\n\n### Token via Environment Variable\n\nAlternatively you can set the environment variable:\n\n```bash\nNOTEABLE_TOKEN=xxxx\n```\n\nand skip assigning the token:\n\n```python\nasync with NoteableClient() as client:\n    await client.ping_rtu()\n```\n\n### Custom Domain\n\n```bash\nNOTEABLE_TOKEN=xxxx\nNOTEABLE_DOMAIN=app.noteable.io\n```\n\nAnd the client will use that particular domain, for custom deployment location. This value defaults to `app.noteable.io`.\n\n```python\nasync with NoteableClient() as client:\n    await client.ping_rtu()\n```\n\n<!-- --8<-- [end:start] -->\n\n## Contributing\n\nSee [CONTRIBUTING.md](./CONTRIBUTING.md).\n\n-------\n\n<p align="center">Open sourced with ❤️ by <a href="https://noteable.io">Noteable</a> for the community.</p>\n\n<img href="https://pages.noteable.io/private-beta-access" src="https://assets.noteable.io/github/2022-07-29/noteable.png" alt="Boost Data Collaboration with Notebooks">\n',
    'author': 'Matt Seal',
    'author_email': 'matt@noteable.io',
    'maintainer': 'Matt Seal',
    'maintainer_email': 'matt@noteable.io',
    'url': 'https://github.com/noteable-io/origami',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
