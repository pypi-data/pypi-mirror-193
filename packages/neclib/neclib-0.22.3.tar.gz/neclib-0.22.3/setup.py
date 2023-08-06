# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neclib',
 'neclib.controllers',
 'neclib.coordinates',
 'neclib.coordinates.observations',
 'neclib.coordinates.pointing_error',
 'neclib.core',
 'neclib.core.data_type',
 'neclib.core.files',
 'neclib.core.formatting',
 'neclib.core.inform',
 'neclib.core.logic',
 'neclib.core.security',
 'neclib.core.type_normalization',
 'neclib.data',
 'neclib.devices',
 'neclib.devices.ad_converter',
 'neclib.devices.attenuator',
 'neclib.devices.da_converter',
 'neclib.devices.encoder',
 'neclib.devices.motor',
 'neclib.devices.power_meter',
 'neclib.devices.signal_generator',
 'neclib.devices.spectrometer',
 'neclib.devices.thermometer',
 'neclib.devices.vacuum_gauge',
 'neclib.devices.weather_station',
 'neclib.recorders',
 'neclib.safety',
 'neclib.simulators',
 'neclib.utils']

package_data = \
{'': ['*'], 'neclib': ['defaults/*']}

install_requires = \
['astropy>=5.2,<6.0',
 'matplotlib>=3.6.2,<4.0.0',
 'necstdb>=0.2.9,<0.3.0',
 'numpy>=1.24,<2.0',
 'ogameasure>=0.5.8,<0.6.0',
 'psutil>=5.9.4,<6.0.0',
 'tomlkit>=0.11.4,<0.12.0',
 'xfftspy>=0.1.3,<0.2.0']

extras_require = \
{':sys_platform == "linux"': ['pyinterface>=1.6,<2.0']}

setup_kwargs = {
    'name': 'neclib',
    'version': '0.22.3',
    'description': 'Pure Python tools for NECST.',
    'long_description': '# neclib\n\n[![PyPI](https://img.shields.io/pypi/v/neclib.svg?label=PyPI&style=flat-square)](https://pypi.org/pypi/neclib/)\n[![Python versions](https://img.shields.io/pypi/pyversions/neclib.svg?label=Python&color=yellow&style=flat-square)](https://pypi.org/pypi/neclib/)\n[![Test status](https://img.shields.io/github/actions/workflow/status/necst-telescope/neclib/test.yml?branch=main&logo=github&label=Test&style=flat-square)](https://github.com/necst-telescope/neclib/actions)\n[![codecov](https://codecov.io/gh/necst-telescope/neclib/branch/main/graph/badge.svg?token=DP2ZTYBOTR)](https://codecov.io/github/necst-telescope/neclib)\n[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg?label=License&style=flat-square)](https://github.com/necst-telescope/neclib/blob/main/LICENSE)\n\nPure Python tools for NECST.\n\n## Features\n\nThis library provides:\n\n- Miscellaneous tools for NECST system.\n- Integration with [IPython](https://ipython.org/) and [AstroPy](https://www.astropy.org/), which provides intuitive interface.\n\n## Installation\n\n```shell\npip install neclib\n```\n\n## Usage\n\nSee the [API Reference](https://necst-telescope.github.io/neclib/_source/neclib.html).\n\n---\n\nThis library is using [Semantic Versioning](https://semver.org).\n',
    'author': 'KaoruNishikawa',
    'author_email': 'k.nishikawa@a.phys.nagoya-u.ac.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://necst-telescope.github.io/neclib/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
