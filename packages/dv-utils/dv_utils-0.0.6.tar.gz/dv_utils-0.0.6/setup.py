# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dv_utils']

package_data = \
{'': ['*']}

install_requires = \
['mkdocs-material>=8.4.2,<9.0.0',
 'mkdocs>=1.3.1,<2.0.0',
 'mkdocstrings-python>=0.7.1,<0.8.0',
 'mkdocstrings>=0.19.0,<0.20.0',
 'python-decouple',
 'rdflib',
 'redis',
 'requests',
 'types-redis',
 'types-requests']

setup_kwargs = {
    'name': 'dv-utils',
    'version': '0.0.6',
    'description': 'DataVillage Python utils for interaction with the middleware and building algo processing code',
    'long_description': '# Utility python library for interaction with data-village middleware\n\n## About\nThis repository contains a set of utilities for the development of application within the cage, especially with respect\nto interfacing with the middleware APIs.\n\n## Release process\nThe version management and git tagging must be done in accordance with the versioning practices described\nin  [`dv-product` README](../dv-product/README.md#versioning-management).\n\n## Deployment\n\n## Code References\n\ncode references for this packages are generated with MkDocs and hosted on Github Pages for this repo:\nhttps://datavillage-me.github.io/dv-utils/\n',
    'author': 'Loic Quertenmont',
    'author_email': 'loic@deeperanalytics.be',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/datavillage-me/dv-utils',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.4,<4',
}


setup(**setup_kwargs)
