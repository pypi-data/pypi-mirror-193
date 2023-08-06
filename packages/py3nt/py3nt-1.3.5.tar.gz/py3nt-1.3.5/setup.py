# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['py3nt',
 'py3nt.core',
 'py3nt.functions',
 'py3nt.functions.binary',
 'py3nt.functions.unary',
 'py3nt.numbers']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2']

setup_kwargs = {
    'name': 'py3nt',
    'version': '1.3.5',
    'description': 'A Number Theory Library for Python 3',
    'long_description': '# `pynt` A Number Theory Library for Python 3\n\n[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/math-projects/pynt/develop.svg)](https://results.pre-commit.ci/latest/github/math-projects/pynt/develop)\n![Workflow for Codecov Action](https://github.com/math-projects/pynt/actions/workflows/codecov.yml/badge.svg)\n[![codecov](https://codecov.io/gh/math-projects/pynt/branch/develop/graph/badge.svg?token=12WCFBI23W)](https://codecov.io/gh/math-projects/pynt)\n[![Documentation Status](https://readthedocs.org/projects/py3nt/badge/?version=latest)](https://py3nt.readthedocs.io/en/latest/?badge=latest)\n',
    'author': 'Masum Billal',
    'author_email': 'billalmasum93@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/math-projects/pynt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
