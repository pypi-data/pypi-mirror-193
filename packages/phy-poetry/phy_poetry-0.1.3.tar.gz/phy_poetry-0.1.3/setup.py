# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['phy_poetry']

package_data = \
{'': ['*']}

install_requires = \
['numpy<1.24.0', 'phy']

setup_kwargs = {
    'name': 'phy-poetry',
    'version': '0.1.3',
    'description': 'Version locking the dependency tree of phy; the suite is less error prone over time',
    'long_description': '# Phy packaged with poetry\n\nVersion locking the dependency tree of `phy` ensures that it can run on any circumstance.\n\n## Install\n```shell\npip install phy-poetry\n```\n',
    'author': 'caniko',
    'author_email': 'canhtart@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
