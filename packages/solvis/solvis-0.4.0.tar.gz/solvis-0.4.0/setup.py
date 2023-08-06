# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['solvis', 'test', 'test.geometry']

package_data = \
{'': ['*'],
 'test': ['fixtures/*',
          'fixtures/MiniInversionSolution/*',
          'fixtures/MiniInversionSolution/ruptures/*',
          'fixtures/MiniInversionSolution/solution/*']}

install_requires = \
['click-plugins>=1.1.1,<2.0.0',
 'geopandas>=0.12.2,<0.13.0',
 'pandas>=1.3.4,<2.0.0',
 'pyproj>=3.3,<4.0',
 'python-dateutil>=2.8.2,<3.0.0',
 'pytz==2021.3',
 'pyvista>=0.37.0,<0.38.0']

extras_require = \
{':extra == "scripts"': ['click>=8.1.3,<9.0.0']}

setup_kwargs = {
    'name': 'solvis',
    'version': '0.4.0',
    'description': 'analysis of opensha modular solution files.',
    'long_description': '# solvis\n\n[![pypi](https://img.shields.io/pypi/v/solvis.svg)](https://pypi.org/project/solvis/)\n[![python](https://img.shields.io/pypi/pyversions/solvis.svg)](https://pypi.org/project/solvis/)\n[![Build Status](https://github.com/GNS-Science/solvis/actions/workflows/dev.yml/badge.svg)](https://github.com/GNS-Science/solvis/actions/workflows/dev.yml)\n[![codecov](https://codecov.io/gh/GNS-Science/solvis/branch/main/graphs/badge.svg)](https://codecov.io/github/GNS-Science/solvis)\n\n\n* Documentation: <https://GNS-Science.github.io/solvis>\n* GitHub: <https://github.com/GNS-Science/solvis>\n* PyPI: <https://pypi.org/project/solvis/>\n* Free software: GPL-3.0-only\n\n# Features / Goals\n\n - analysis of opensha modular solution files.\n - opensha modular documentation\n - pandas, geopanda references\n\nFrom a typical modular opensha Inversion Solution archive, we want to produce views that allow deep exploration \nof the solution and rupture set characteristics. Features:\n\n - [ ] user can choose from regions already defined in the solution\n - user can select ruptures matching \n    - [x] parent fault\n    - [ ] named fault (fault system)\n    - [ ] constraint region (from TargetMFDs)\n - [x] user can create new region polygons\n - [ ] user can compare selections (e.g. Wellington East vs Wellington CBD vs Hutt Valley) \n - for a given query result show me dimensions...\n    - mag, length, area, rate, section count, parent fault count, jump-length, jump angles, slip (various), partication, nucleation \n    - filter, group on any of the dimensions\n\n\n## From here the user can answer questions like ....\n\n - create a MFD histogram in 0.01 bins from 7.0 to 7.30 (3O bins) for the WHV fault system\n - list all ruptures between 7.75 and 8.25, involving the TVZ, ordered by rupture-length\n - given a user-defined-function udfRuptureComplexity(rupture) rank ruptures in Region X by complexity, then by magnitude\n\n  - regional MFD\n      - [x] participation (sum of rate) for every rupture though a point\n      - [ ] nucleation/blame/culpability rate summed over the region\n           normalised by the area of an area (region, named fault)\n\n\n## Install (Linux, OSX)\n\n```\npoetry add solvis\n```\n\n### Windows Installation with pipwin (CHECK)\n\nThis information predates poetry and has not been check since ...\n\nYou will have to delete the fiona and shapely lines from requirements.txt, then run the following lines:\npip3 install -r requirements\n\n```commandline\npip install pipwin\npipwin install gdal\npipwin install fiona\npipwin install shapely\npip install -r requirements.txt\n```\n\n## Run\n\n```\npython3 -m demo\n\nor python3 demo.py\n```\n\n## Plotting\n\n\nf = plt.figure()\n#nx = int(f.get_figwidth() * f.dpi)\n#ny = int(f.get_figheight() * f.dpi)\nf.figimage(data)\nplt.show()',
    'author': 'Chris Chamberlain',
    'author_email': 'chrisbc@artisan.co.nz',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
