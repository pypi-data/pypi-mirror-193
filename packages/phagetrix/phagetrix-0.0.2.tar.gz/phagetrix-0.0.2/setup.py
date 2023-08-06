# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['phagetrix']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['phagetrix = phagetrix.exec:main']}

setup_kwargs = {
    'name': 'phagetrix',
    'version': '0.0.2',
    'description': 'Optimizer for degenerate codon use in phage library generation',
    'long_description': '[![check](https://github.com/retospect/phagetrix/actions/workflows/check.yml/badge.svg)](https://github.com/retospect/phageterix/actions/workflows/check.yml)\n\n# Phagetrix\n\nA codon optimizer for phage display library generation.\n\n\n',
    'author': 'Reto Stamm',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/retospect/phagetrix',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
}


setup(**setup_kwargs)
