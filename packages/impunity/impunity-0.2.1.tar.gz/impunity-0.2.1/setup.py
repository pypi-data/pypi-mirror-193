# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['impunity']

package_data = \
{'': ['*']}

install_requires = \
['Pint>=0.19.2', 'astor>=0.8.1,<0.9.0']

extras_require = \
{':python_version < "3.10"': ['typing-extensions>=4.2.0,<5.0.0']}

setup_kwargs = {
    'name': 'impunity',
    'version': '0.2.1',
    'description': 'Static checking for consistency of physical units',
    'long_description': 'None',
    'author': 'Antoine Chevrot',
    'author_email': 'antoine.chevrot@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
