# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sc_permut']

package_data = \
{'': ['*']}

install_requires = \
['keras==2.4.3',
 'kopt==0.1.0',
 'py4j>=0.10.9.7,<0.11.0.0',
 'pyyaml==5.3.1',
 'scanpy==1.6.0',
 'tensorflow==2.3.1']

entry_points = \
{'console_scripts': ['sc_permut = sc_permut.__main__:main']}

setup_kwargs = {
    'name': 'sc-permut',
    'version': '0.1.0',
    'description': '',
    'long_description': 'None',
    'author': 'becavin-lab',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
