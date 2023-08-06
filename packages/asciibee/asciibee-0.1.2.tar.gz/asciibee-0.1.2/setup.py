# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asciibee']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=9.4,<10.0', 'numpy>=1.24.2,<2.0.0']

entry_points = \
{'console_scripts': ['asciibee = asciibee.main:main']}

setup_kwargs = {
    'name': 'asciibee',
    'version': '0.1.2',
    'description': 'An image-to-ascii-art converter',
    'long_description': '# asciibee\n\nAn image-to-ascii-art converter\n\n## Description\n\nThe default settings are tuned to work well with fine art. Play with different\nshaders, image squaring, and value inversion for different results.\n\nScaling is done by reducing the image by a factor of 2 until it fits in the\nterminal window or the width is below the max width you specify.\n\nEach ASCII character is chosen by expanding the range of pixel values to the\nfull range of characters. For example, if the darkest value in the original\nimage is 100 (of 255), and the lightest 230 (of 255), then 100 becomes the "new"\n0 (and darkest char) and 230 the new 255 (and lightest char). You can provide\nthe -1 flag to use exact values instead.\n\n## Installation\n\n`$ pip install asciibee`\n\n## Usage\n\nThe best way to learn how to use the app is via the help text:\n\n`$ asciibee --help`\n\nThe most simple command is passing in a path to an image file:\n\n`$ asciibee ~/Downloads/starrynight.png`\n\nYou can use it as an importable module as well.\n\n```python\nfrom asciibee.image import AsciiImage\nimage = AsciiImage(\'/Users/jnakama/Downloads/port.jpeg\')\nimage.convert()  # Converts the image to a matrix of ASCII characters\nimage.ascii_matrix # Here\nimage.show()  # Prints the characters\n```\n\n## Development\n\nThe build system and package manager is [poetry](https://python-poetry.org/).\n\nThe easiest way to run the app locally:\n\n`$ poetry run python -m asciibee.main <path_to_image>`\n\nYou can also install the deps and run it without the `poetry run` prefix.\n',
    'author': 'Jamey Nakama',
    'author_email': 'nakamajamey@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
