# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cgekit']

package_data = \
{'': ['*']}

install_requires = \
['cgepy>=0.6.3,<0.7.0']

setup_kwargs = {
    'name': 'cgekit',
    'version': '0.1.1',
    'description': 'Additional tools for the cgePy library',
    'long_description': '',
    'author': 'catbox305',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
