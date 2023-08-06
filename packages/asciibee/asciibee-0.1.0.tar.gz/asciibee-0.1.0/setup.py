# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asciibee']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.4,<10.0', 'numpy>=1.24.2,<2.0.0']

setup_kwargs = {
    'name': 'asciibee',
    'version': '0.1.0',
    'description': '',
    'long_description': '# asciibee\n\nAn image-to-ascii-art converter\n',
    'author': 'Jamey Nakama',
    'author_email': 'nakamajamey@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
