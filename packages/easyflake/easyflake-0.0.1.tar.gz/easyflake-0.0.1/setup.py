# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['easyflake']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'easyflake',
    'version': '0.0.1',
    'description': '',
    'long_description': '# EasyFlake\n\nAn unique ID Generator\n',
    'author': 'tsuperis',
    'author_email': 'tsuperis@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
