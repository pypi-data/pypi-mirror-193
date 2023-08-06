# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyfunctools']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyfunctools',
    'version': '0.6.0',
    'description': 'pyfunctools - Functional programming toolkit',
    'long_description': '# Pyfunctools\n\nPyfunctools is a module that provides functions, methods and classes that help in the creation of projects in python, bringing functional and object-oriented programming methods.\n\n[![Documentation Status](https://readthedocs.org/projects/pyfunctools/badge/?version=latest)](https://pyfunctools.readthedocs.io/en/latest/?badge=latest)\n[![Python versions](https://img.shields.io/pypi/pyversions/pyfunctools.svg)](https://pypi.python.org/pypi/pyfunctools/)\n[![downloads](https://img.shields.io/pypi/dm/pyfunctools.svg)](https://pypi.org/project/pyfunctools/)\n[![PyPI version](https://badge.fury.io/py/pyfunctools.svg)](https://badge.fury.io/py/pyfunctools)\n[![GitHub stars](https://img.shields.io/github/stars/natanfeitosa/pyfunctools.svg)](https://github.com/natanfeitosa/pyfunctools/stargazers)\n[![Open Source Helpers](https://www.codetriage.com/natanfeitosa/pyfunctools/badges/users.svg)](https://www.codetriage.com/natanfeitosa/pyfunctools)\n[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/natanfeitosa)\n\n## Instalation\n\nVia PIP (recommended):\n```sh\npip install pyfunctools\n```\n\nVia GitHub:\n```sh\ngit clone https://github.com/natanfeitosa/pyfunctools.git && cd pyfunctools && pip install .\n```\n<!-- \n## Development\n\n> Makefile commands so far only available for linux\n\n<br>\n\n```make init``` install development dependencies.\n\nRun ```make auto_doc``` when adding a new submodule.\n\nTo create the documentation based on the docstrings, just run ```make gen_docs```.\n\nTest the HTML documentation locally with the ```make server``` command.\n\nThe ```make all``` command runs the last two automatically. -->\n',
    'author': 'Natan Santos',
    'author_email': 'natansantosapps@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
