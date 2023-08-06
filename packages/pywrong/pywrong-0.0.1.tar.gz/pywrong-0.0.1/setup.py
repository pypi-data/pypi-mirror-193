# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pywrong']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0',
 'semantic-version>=2.10.0,<3.0.0',
 'typeguard>=3.0.0b2,<4.0.0']

extras_require = \
{'debug': ['ipdb>=0.13.11,<0.14.0']}

entry_points = \
{'console_scripts': ['pywrong = pywrong.server:serve']}

setup_kwargs = {
    'name': 'pywrong',
    'version': '0.0.1',
    'description': 'A wrapper for pyright',
    'long_description': '# pywrong\nA wrapper for PyRight\n',
    'author': 'Amit Prakash Ambasta',
    'author_email': 'amit.prakash.ambasta@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
