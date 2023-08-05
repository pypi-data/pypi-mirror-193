# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pesel']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['pesel = pesel.main:cli']}

setup_kwargs = {
    'name': 'pesel',
    'version': '0.4.0',
    'description': '',
    'long_description': 'None',
    'author': 'Jakub Spórna',
    'author_email': 'jakub.sporna@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
