# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_cpf']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['CPF = simple_cpf.simple_cpf:CPF']}

setup_kwargs = {
    'name': 'simple-cpf',
    'version': '0.1.2',
    'description': 'A simple script to manipulate and validate CPF',
    'long_description': '# cpf\n',
    'author': 'czargodoi',
    'author_email': 'czargodoi@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
