# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['googletv']

package_data = \
{'': ['*']}

install_requires = \
['adb-shell[async]>=0.4.3,<0.5.0']

setup_kwargs = {
    'name': 'googletv',
    'version': '0.0.2',
    'description': '',
    'long_description': '# python-googletv',
    'author': 'Sören Oldag',
    'author_email': 'soeren_oldag@freenet.de',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10',
}


setup(**setup_kwargs)
