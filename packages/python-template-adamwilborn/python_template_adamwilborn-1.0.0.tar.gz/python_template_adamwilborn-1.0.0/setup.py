# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_template']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-template-adamwilborn',
    'version': '1.0.0',
    'description': '',
    'long_description': '',
    'author': 'Adam Wilborn',
    'author_email': 'adamw97@vt.edu',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
