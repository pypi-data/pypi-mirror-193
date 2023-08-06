# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sand',
 'sand.commands',
 'sand.controllers',
 'sand.controllers.helpers',
 'sand.models',
 'sand.plugins',
 'sand.plugins.drepr',
 'sand.plugins.drepr.raw_transformations']

package_data = \
{'': ['*'],
 'sand': ['www/*', 'www/static/css/*', 'www/static/js/*', 'www/static/media/*']}

install_requires = \
['Flask>=2.2.2,<3.0.0',
 'drepr>=2.10.0,<3.0.0',
 'gena>=1.6.4,<2.0.0',
 'kgdata>=3.4.2,<4.0.0',
 'lat_lon_parser>=1.3.0,<2.0.0',
 'loguru>=0.6.0,<0.7.0',
 'orjson>=3.8.2,<4.0.0',
 'peewee>=3.15.2,<4.0.0',
 'python-dotenv>=0.19.0,<0.20.0',
 'sem-desc>=4.4.2,<5.0.0',
 'sm-grams>=2.1.7,<3.0.0',
 'tornado>=6.2,<7.0']

entry_points = \
{'console_scripts': ['sand = sand.__main__:cli']}

setup_kwargs = {
    'name': 'web-sand',
    'version': '2.1.10',
    'description': 'UI for browsing/editing semantic descriptions',
    'long_description': '<h1 align="center">SAND</h1>\n\n<div align="center">\n\n![PyPI](https://img.shields.io/pypi/v/web-sand)\n![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)\n[![GitHub Issues](https://img.shields.io/github/issues/usc-isi-i2/sand.svg)](https://github.com/usc-isi-i2/sand/issues)\n![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)\n[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)\n\n</div>\n\n## Table of Contents\n\n- [Introduction](#introduction)\n- [Installation](#installation)\n\n## Introduction\n\nSAND is an application to annotate semantic descriptions of tables and (optionally) linked records in tables to a target knowledge graph, then it can automatically export the table data to RDF, JSON-LD, etc. It also does basic data cleaning automatically based on the annotated semantic descriptions. SAND is designed to be customizable: you can plug in a new semantic modeling algorithm (which generates a semantic description automatically) or different knowledge graphs as long as you have a suitable plugin implemented SAND\'s plugin interface.\n\nMoreover, SAND offers an internal KG browsing and table filtering so you can interactively browsing and modeling your tables.\n\nFor a demo, please see: our [demo paper](./docs/paper.pdf), [demo video](https://github.com/usc-isi-i2/sand/wiki/Demo).\n\n<!-- For more documentation, please see [not available yet](). -->\n\n## Installation\n\nInstall from pip: `pip install -U web-sand`\n\n## Usage\n\n1. Initialize database: `sand init -d <dbfile>`. For example: `sand init -d ./data/sand.db`\n2. Start the webserver: `sand start -d <dbfile> --externaldb <folder_of_ent_and_ont_db>`\n3. Open the URL: `http://localhost:5524`\n\nFor example, checkout [server.sh](./server.sh)\n\n## Development\n\n0. cd to `www`\n1. Install `yarn` and [`yalc`](https://github.com/wclr/yalc)\n2. Install dependencies: `yarn install`\n3. Start development server: `yarn start`. Then, access development server at: `http://127.0.0.1:3000`.\n4. Build production files: `yarn build`\n5. Build library files and publish to private index (only if you are released `sand` as a library): `yarn build:lib && yalc public --private`\n',
    'author': 'Binh Vu',
    'author_email': 'binh@toan2.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/usc-isi-i2/sand',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<3.11',
}


setup(**setup_kwargs)
