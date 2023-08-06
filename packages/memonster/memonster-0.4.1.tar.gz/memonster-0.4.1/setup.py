# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['memonster']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'memonster',
    'version': '0.4.1',
    'description': 'Python memory thing',
    'long_description': '',
    'author': 'SirOlaf',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/SirOlaf/memonster',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
