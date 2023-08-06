# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['kernel_sidecar', 'kernel_sidecar.models']

package_data = \
{'': ['*']}

install_requires = \
['jupyter-client>=7.3.4', 'pydantic>=1.10.4,<2.0.0']

setup_kwargs = {
    'name': 'kernel-sidecar',
    'version': '0.2.0',
    'description': 'A sidecar ',
    'long_description': '<p align="center">\nKernel Sidecar\n</p>\n\n<p align="center">\n<img alt="Pypi" src="https://img.shields.io/pypi/v/kernel-sidecar">\n<a href="https://github.com/kafonek/kernel-sidecar/actions/workflows/tests.yaml">\n    <img src="https://github.com/kafonek/kernel-sidecar/actions/workflows/tests.yaml/badge.svg" alt="Tests" />\n</a>\n<img alt="Python versions" src="https://img.shields.io/pypi/pyversions/kernel-sidecar">\n</p>\n',
    'author': 'Matt Kafonek',
    'author_email': 'matt.kafonek@noteable.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kafonek/kernel-sidecar',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
