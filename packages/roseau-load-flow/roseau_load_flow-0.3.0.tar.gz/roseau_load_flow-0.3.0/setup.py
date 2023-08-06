# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['load_flow',
 'load_flow.io',
 'load_flow.models',
 'load_flow.models.lines',
 'load_flow.models.loads',
 'load_flow.models.transformers',
 'load_flow.utils']

package_data = \
{'': ['*']}

install_requires = \
['geopandas>=0.10.2',
 'numpy>=1.21.5',
 'pandas>=1.4.0',
 'pint>=0.19.2',
 'regex>=2022.1.18',
 'requests>=2.28.1',
 'shapely>=2.0.0']

setup_kwargs = {
    'name': 'roseau-load-flow',
    'version': '0.3.0',
    'description': 'Three-phase load flow solver',
    'long_description': '# Roseau Load Flow #\n\n![CI](https://github.com/RoseauTechnologies/Roseau_Load_Flow/workflows/CI/badge.svg)\n[![Documentation](https://github.com/RoseauTechnologies/Roseau_Load_Flow/actions/workflows/doc.yml/badge.svg)](https://github.com/RoseauTechnologies/Roseau_Load_Flow/actions/workflows/doc.yml)\n[![pre-commit](https://github.com/RoseauTechnologies/Roseau_Load_Flow/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/RoseauTechnologies/Roseau_Load_Flow/actions/workflows/pre-commit.yml)\n\n*Roseau Load Flow* is a highly capable three-phase load flow solver. This project is compatible\nwith Python 3.9 and above.\n\nPlease take a look at our documentation to see how to install and use `roseau_load_flow`.\n\n* [Installation](https://roseautechnologies.github.io/Roseau_Load_Flow/installation.html)\n* [Usage](https://roseautechnologies.github.io/Roseau_Load_Flow/notebooks/Getting_Started.html)\n\n# Accessing the solver #\n\nThis is the client library for the *Roseau Load Flow* solver. To use the solver, you need to sign\nup for an account. For inquiry, please contact us at contact@roseautechnologies.com.\n\n# Bug reports / Feature requests #\n\nIf you find a bug or have a feature request, please open an issue on the\n[GitHub](https://github.com/RoseauTechnologies/Roseau_Load_Flow/issues)\n',
    'author': 'Ali Hamdan',
    'author_email': 'ali.hamdan@roseautechnologies.com',
    'maintainer': 'Ali Hamdan',
    'maintainer_email': 'ali.hamdan@roseautechnologies.com',
    'url': 'https://github.com/RoseauTechnologies/Roseau_Load_Flow/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
