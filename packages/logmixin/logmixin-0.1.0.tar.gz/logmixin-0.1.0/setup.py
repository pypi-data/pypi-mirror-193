# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['logmixin']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'logmixin',
    'version': '0.1.0',
    'description': 'Defines a mixin class allowing classes to get a logger with the name of the module, class and method it was called from.',
    'long_description': 'None',
    'author': 'Sam Mathias',
    'author_email': 'samuel.mathias@childrens.harvard.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
