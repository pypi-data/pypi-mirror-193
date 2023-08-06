# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kng']

package_data = \
{'': ['*']}

install_requires = \
['httpx>=0.23.3,<0.24.0', 'toml>=0.10.2,<0.11.0']

entry_points = \
{'console_scripts': ['pump = pump:main']}

setup_kwargs = {
    'name': 'kng',
    'version': '0.2.0',
    'description': 'handy utility functions collection',
    'long_description': '# kng\n\n[![ci-badge]][ci-url] [![pypi-badge]][pypi-url] [![coverage-badge]][coverage-url] ![py-ver-badge] [![MIT-badge]][MIT-url] [![black-badge]][black-url]\n\n[ci-badge]: https://github.com/hoishing/kng/actions/workflows/ci.yml/badge.svg\n[ci-url]: https://github.com/hoishing/kng/actions/workflows/ci.yml\n[coverage-badge]: https://hoishing.github.io/kng/assets/coverage-badge.svg\n[coverage-url]: https://hoishing.github.io/kng/assets/coverage/\n[MIT-badge]: https://img.shields.io/github/license/hoishing/kng\n[MIT-url]: https://opensource.org/licenses/MIT\n[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg\n[black-url]: https://github.com/psf/black\n[py-ver-badge]: https://img.shields.io/pypi/pyversions/pipable\n[pypi-badge]: https://img.shields.io/pypi/v/kng\n[pypi-url]: https://pypi.org/project/kng\n\n> a collection of python utility functions for daily use\n\n🔗 [source code](https://github.com/hoishing/kng)\n\n## Quick Start\n\n- `pip install kng`\n\nsee [documentation] for complete list of utility functions\n\n[documentation]: https://hoishing.github.io/kng\n\n## Need Help?\n\nOpen a [github issue] or ping me on [Twitter] ![twitter-icon]\n\n[github issue]: https://github.com/hoishing/kng/issues\n[Twitter]: https://twitter.com/hoishing\n[twitter-icon]: https://api.iconify.design/logos/twitter.svg?width=20\n',
    'author': 'Kelvin Ng',
    'author_email': 'hoishing@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://hoishing.github.io/kng',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
