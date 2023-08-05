# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['simple_cog_client']

package_data = \
{'': ['*']}

install_requires = \
['pillow>=9.4.0,<10.0.0', 'requests>=2.28.2,<3.0.0']

setup_kwargs = {
    'name': 'simple-cog-client',
    'version': '0.1.0',
    'description': '',
    'long_description': '',
    'author': 'Carlos Aranda',
    'author_email': 'carlos.aranda@ksms.mx',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
