# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['securecred']

package_data = \
{'': ['*']}

install_requires = \
['pyaes>=1.6.1,<2.0.0', 'pytest==5.2']

setup_kwargs = {
    'name': 'securecred',
    'version': '0.1.0',
    'description': 'Securely write/read your credentials/messages in/from files using AES encryption. (depends only on pyaes - a small, pure-python package thus platform independent)',
    'long_description': None,
    'author': 'Gwang-Jin Kim',
    'author_email': 'gwang.jin.kim.phd@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
