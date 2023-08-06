# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commonfate_provider',
 'commonfate_provider.runtime',
 'commonfate_provider.runtime.tests']

package_data = \
{'': ['*']}

install_requires = \
['pydantic==1.10.2', 'toml==0.10.2', 'typing-extensions>=4.5.0,<5.0.0']

setup_kwargs = {
    'name': 'commonfate-provider',
    'version': '0.1.26',
    'description': 'This is the core Provider framework on top of which Access Provider are written.',
    'long_description': '# commonfate-provider-core\nCommonfate Provider Core Python Package\n',
    'author': 'Chris Norman',
    'author_email': 'chris@commonfate.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
