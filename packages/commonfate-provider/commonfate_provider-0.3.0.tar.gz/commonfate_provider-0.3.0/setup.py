# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['commonfate_provider',
 'commonfate_provider.cli',
 'commonfate_provider.runtime',
 'commonfate_provider.runtime.tests']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'pydantic==1.10.2',
 'toml==0.10.2',
 'typing-extensions>=4.5.0,<5.0.0']

entry_points = \
{'console_scripts': ['commonfate-provider-py = '
                     'commonfate_provider.cli.main:cli']}

setup_kwargs = {
    'name': 'commonfate-provider',
    'version': '0.3.0',
    'description': 'This is the core Provider framework on top of which Access Provider are written.',
    'long_description': "# commonfate-provider-core\n\nCommonfate Provider Core Python Package\n\n## Building a development version\n\nWhen working on the Common Fate Provider framework it can be useful to use a development build of this package in an Access Provider. To do so run:\n\n```\npoetry build\n```\n\nwhich will create a `dist` folder containing the package:\n\n```\ndist\n├── commonfate_provider-0.1.5-py3-none-any.whl\n└── commonfate_provider-0.1.5.tar.gz\n```\n\nYou can then install this package locally via `pip` in the Access Provider you'd like to use it with:\n\n```bash\n# from the Access Provider repository\nsource .venv/bin/activate\npip install ../commonfate-provider-core/dist/commonfate_provider-0.1.5.tar.gz\n```\n",
    'author': 'Chris Norman',
    'author_email': 'chris@commonfate.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
