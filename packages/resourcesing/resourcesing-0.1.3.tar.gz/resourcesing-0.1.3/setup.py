# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resourcesing']

package_data = \
{'': ['*']}

install_requires = \
['daemonprocessing>=0.1.1,<0.2.0']

setup_kwargs = {
    'name': 'resourcesing',
    'version': '0.1.3',
    'description': '',
    'long_description': '',
    'author': 'jawide',
    'author_email': '596929059@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
