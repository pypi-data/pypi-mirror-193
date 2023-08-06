# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['verlib', 'verlib.integrations']

package_data = \
{'': ['*']}

install_requires = \
['schema>=0.7.5,<0.8.0']

extras_require = \
{'django': ['django>=4.1.7,<5.0.0'], 'flask': ['flask>=2.2.3,<3.0.0']}

setup_kwargs = {
    'name': 'pyverlib',
    'version': '0.1.1',
    'description': 'library for building RPC APIs',
    'long_description': '',
    'author': 'stackswithans',
    'author_email': 'stexor12@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
