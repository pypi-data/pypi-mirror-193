# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['astrodown']

package_data = \
{'': ['*']}

install_requires = \
['pyodide-http>=0.2.0,<0.3.0']

setup_kwargs = {
    'name': 'astrodown',
    'version': '0.1.4',
    'description': '',
    'long_description': None,
    'author': 'Qiushi Yan',
    'author_email': 'qiushi.yann@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
