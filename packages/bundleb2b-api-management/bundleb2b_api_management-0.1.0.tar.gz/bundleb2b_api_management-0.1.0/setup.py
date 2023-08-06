# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bundleb2b_api_management',
 'bundleb2b_api_management.company',
 'bundleb2b_api_management.dataclass_functions',
 'bundleb2b_api_management.user']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.28.2,<3.0.0', 'retry>=0.9.2,<0.10.0']

setup_kwargs = {
    'name': 'bundleb2b-api-management',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Craig Novak',
    'author_email': 'craig.novak@coedistributing.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
