# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mechlib']

package_data = \
{'': ['*']}

install_requires = \
['protobuf<4.0.0',
 'roboflow>=0.2.29,<0.3.0',
 'torch>=1.13.1,<2.0.0',
 'torchvision>=0.14.1,<0.15.0',
 'ultralytics>=8.0.20,<9.0.0']

entry_points = \
{'console_scripts': ['mechbattle = mechlib.mechbattle:start']}

setup_kwargs = {
    'name': 'mechlib',
    'version': '0.1.0',
    'description': 'Mech Library for MechBattles',
    'long_description': 'None',
    'author': 'Ric Pruss',
    'author_email': 'ricpruss@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<=3.11',
}


setup(**setup_kwargs)
