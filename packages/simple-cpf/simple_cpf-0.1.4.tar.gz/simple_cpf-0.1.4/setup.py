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
    'version': '0.1.4',
    'description': 'A simple script to manipulate and validate CPF',
    'long_description': "# Simple CPF\n\nA simple package to validate and format the CPF - _Brazil Identification Card_.   \n\n## Installation\n\n```bash\npip install simple-cpf\n```\n\n## How to use\n\n```python\nimport simple_cpf.simple_cpf import CPF\n\n# validating a cpf\nCPF.is_valid('117.762.459-11')  # True\nCPF.is_valid('117.762.459-19')  # False\n\n# generating a fake cpf\nCPF.fake()                      # '917.350.558-75'\n\n# formatting a valid cpf\nCPF.formatted('10757246354')    # '107.572.463-54'\n                                # in case of invalid cpf, it will return:\n                                # 'Enter a valid CPF.'\n```\n\n## Made by:\ncesargodoi  -  https://github.com/cesargodoi/simple_cpf",
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
