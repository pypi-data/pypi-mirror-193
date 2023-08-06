# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tum_esm_em27_metadata']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.10.4,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'types-requests>=2.28.11.8,<3.0.0.0']

setup_kwargs = {
    'name': 'tum-esm-em27-metadata',
    'version': '0.1.0',
    'description': "single source of truth for ESM's EM27 measurement logistics",
    'long_description': 'None',
    'author': 'Moritz Makowski',
    'author_email': 'moritz.makowski@tum.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tum-esm/em27-metadata',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
