# asciibee

An image-to-ascii-art converter

## Description

The default settings are tuned to work well with fine art. Play with different
shaders, image squaring, and value inversion for different results.

Scaling is done by reducing the image by a factor of 2 until it fits in the
terminal window or the width is below the max width you specify.

Each ASCII character is chosen by expanding the range of pixel values to the
full range of characters. For example, if the darkest value in the original
image is 100 (of 255), and the lightest 230 (of 255), then 100 becomes the "new"
0 (and darkest char) and 230 the new 255 (and lightest char). You can provide
the -1 flag to use exact values instead.

## Installation

`$ pip install asciibee`

## Usage

The best way to learn how to use the app is via the help text:

`$ asciibee --help`

The most simple command is passing in a path to an image file:

`$ asciibee ~/Downloads/starrynight.png`

You can use it as an importable module as well.

```python
from asciibee.image import AsciiImage
image = AsciiImage('/Users/jnakama/Downloads/port.jpeg')
image.convert()  # Converts the image to a matrix of ASCII characters
image.ascii_matrix # Here
image.show()  # Prints the characters
```

## Development

The build system and package manager is [poetry](https://python-poetry.org/).

The easiest way to run the app locally:

`$ poetry run python -m asciibee.main <path_to_image>`

You can also install the deps and run it without the `poetry run` prefix.
