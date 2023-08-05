# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['xtream_diamonds',
 'xtream_diamonds.challenge3',
 'xtream_diamonds.challenge4',
 'xtream_diamonds.challenge4.endpoints']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.92.0,<0.93.0',
 'pandas>=1.5.3,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'scikit-learn>=1.2.1,<2.0.0',
 'uvicorn[standard]>=0.20.0,<0.21.0',
 'xgboost>=1.7.3,<2.0.0']

entry_points = \
{'console_scripts': ['assignment-price = '
                     'xtream_diamonds.challenge4.request:post',
                     'assignment-server = xtream_diamonds.challenge4.main:main',
                     'assignment-train = xtream_diamonds.challenge3.main:main']}

setup_kwargs = {
    'name': 'xtream-diamonds',
    'version': '0.3.0',
    'description': 'Xtream Data Science Interview Assignment',
    'long_description': '',
    'author': 'dpaletti',
    'author_email': 'dpaletti@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
