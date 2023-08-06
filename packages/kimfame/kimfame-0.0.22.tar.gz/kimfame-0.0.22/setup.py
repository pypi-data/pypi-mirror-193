# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kimfame']

package_data = \
{'': ['*']}

install_requires = \
['faker>=17.0.0,<18.0.0']

setup_kwargs = {
    'name': 'kimfame',
    'version': '0.0.22',
    'description': 'PyPI test project',
    'long_description': '# Kimfame\n\nPyPI Test Project',
    'author': 'kimfame',
    'author_email': 'renownkim@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kimfame/kimfame',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
