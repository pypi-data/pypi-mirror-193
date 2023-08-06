# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['flet_core']

package_data = \
{'': ['*']}

install_requires = \
['repath>=0.9.0,<0.10.0']

extras_require = \
{':python_version < "3.8"': ['typing-extensions>=4.4.0,<5.0.0']}

setup_kwargs = {
    'name': 'flet-core',
    'version': '0.5.0.dev1225',
    'description': 'Flet core library',
    'long_description': '# Flet core library\n\nThe library is the foundation of Flet framework and is not intended to be used directly.\n\nInstall [`flet` module](https://pypi.org/project/flet/) to use Flet framework.',
    'author': 'Appveyor Systems Inc.',
    'author_email': 'hello@flet.dev',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
