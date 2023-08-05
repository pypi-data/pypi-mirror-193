# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['github_restore']

package_data = \
{'': ['*']}

install_requires = \
['prometheus_client>=0.16.0,<0.17.0', 'requests>=2.28.2,<3.0.0']

entry_points = \
{'console_scripts': ['github-restore = github_restore.main:main']}

setup_kwargs = {
    'name': 'github-restore',
    'version': '0.0.1',
    'description': '',
    'long_description': '# github-restore\n',
    'author': 'Karina5005',
    'author_email': 'karinaanisimova23062001@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
