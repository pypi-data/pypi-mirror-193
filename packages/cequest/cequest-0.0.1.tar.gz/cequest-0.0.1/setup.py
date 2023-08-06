# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cequest']

package_data = \
{'': ['*']}

install_requires = \
['Brotli>=1.0.9,<2.0.0',
 'Flask>=2.2.0,<3.0.0',
 'numpy>=1.22.2,<2.0.0',
 'replit>=3.2.4,<4.0.0',
 'selenium>=4.8.2,<5.0.0',
 'urllib3>=1.26.12,<2.0.0']

setup_kwargs = {
    'name': 'cequest',
    'version': '0.0.1',
    'description': 'Advanced python-based request library with proxy support, exception handling & more.',
    'long_description': None,
    'author': 'ecriminals',
    'author_email': 'bio@fbi.ac',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10.0,<3.11',
}


setup(**setup_kwargs)
