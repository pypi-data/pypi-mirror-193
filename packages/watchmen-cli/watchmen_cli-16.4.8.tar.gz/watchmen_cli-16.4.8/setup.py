# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['watchmen_cli', 'watchmen_cli.common', 'watchmen_cli.service']

package_data = \
{'': ['*']}

install_requires = \
['fire>=0.4.0,<0.5.0', 'requests>=2.27.1,<3.0.0', 'watchmen-utilities==16.4.8']

setup_kwargs = {
    'name': 'watchmen-cli',
    'version': '16.4.8',
    'description': '',
    'long_description': 'None',
    'author': 'botlikes',
    'author_email': '75356972+botlikes456@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
