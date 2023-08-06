# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['planetcantile', 'planetcantile.data']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'morecantile>=3.2.1,<4.0.0',
 'pyproj>=3.4.0,<4.0.0',
 'pytest>=7.2.0,<8.0.0']

setup_kwargs = {
    'name': 'planetcantile',
    'version': '0.1.0',
    'description': 'TMS tilesets for Planets',
    'long_description': '# Planetcantile\n\n\nAdds TileMatrixSets for other planets.\nAims to be home to a wide range of tilesets for the Moon, Mars, and more.\n\nIntegrates with [morecantile](https://github.com/developmentseed/morecantile), ideally should allow downstream projects to benefit from additional TMSs defined here.\n\nDefinitions go into the generate.py script to have fine grain control, alternatively json files can just be added directly to the data directory.\n\n',
    'author': 'Andrew Annex',
    'author_email': 'ama6fy@virginia.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/AndrewAnnex/planetcantile',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
