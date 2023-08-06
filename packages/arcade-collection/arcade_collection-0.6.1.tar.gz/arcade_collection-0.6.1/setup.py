# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['arcade_collection', 'arcade_collection.input', 'arcade_collection.output']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.2,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'prefect>=2.8.2,<3.0.0',
 'scikit-image>=0.19.3,<0.20.0',
 'simulariumio>=1.7.0,<2.0.0']

setup_kwargs = {
    'name': 'arcade-collection',
    'version': '0.6.1',
    'description': 'Collection of tasks for working with ARCADE.',
    'long_description': '[![Build Status](https://github.com/bagherilab/arcade-collection/workflows/build/badge.svg)](https://github.com/bagherilab/arcade-collection/actions?query=workflow%3Abuild)\n[![Codecov](https://img.shields.io/codecov/c/gh/bagherilab/arcade-collection?token=OXH1XGZOCI)](https://codecov.io/gh/bagherilab/arcade-collection)\n[![Lint Status](https://github.com/bagherilab/arcade-collection/workflows/lint/badge.svg)](https://github.com/bagherilab/arcade-collection/actions?query=workflow%3Alint)\n[![Documentation](https://github.com/bagherilab/arcade-collection/workflows/documentation/badge.svg)](https://bagherilab.github.io/arcade-collection/)\n[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n',
    'author': 'Jessica S. Yu',
    'author_email': 'jesyu@uw.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
