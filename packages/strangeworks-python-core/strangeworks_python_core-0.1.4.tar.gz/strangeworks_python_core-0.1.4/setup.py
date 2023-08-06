# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['strangeworks_core',
 'strangeworks_core.config',
 'strangeworks_core.errors',
 'strangeworks_core.platform',
 'strangeworks_core.types']

package_data = \
{'': ['*']}

install_requires = \
['gql>=3.4.0,<4.0.0',
 'requests-toolbelt>=0.10.1,<0.11.0',
 'requests>=2.28.2,<3.0.0',
 'tomlkit>=0.11.6,<0.12.0']

setup_kwargs = {
    'name': 'strangeworks-python-core',
    'version': '0.1.4',
    'description': 'Strangeworks Core provides the infrastructure to interact with the platform.',
    'long_description': '# Strangeworks Python Core Library\n\nThe Strangeworks Python Core Library provides commonly used things.\n\n## Installation\n\nInstall using `poetry`\n\n```\npip install poetry\npoetry install\n```\n\n## Tests\n\nTest using pytest\n\n```\npoetry run pytest tests\n```\n\n## Set up dev pre-commit hooks:\n\nthe pre-commit hook registered takes care of linting, formatting, etc.\n\n```\n poetry run pre-commit install\n```\n\n## Bump version\n\nBump version with [poetry](https://python-poetry.org/docs/cli/#version).\n\n```\npoetry version [patch, minor, major]\n```\n\n## Update packages\n\nUpdate <package> version\n\n```\npoetry update <package>\n```\n\nUpdate all packages\n\n```\npoetry update\n```\n',
    'author': 'Strange Devs',
    'author_email': 'hello@strangeworks.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
