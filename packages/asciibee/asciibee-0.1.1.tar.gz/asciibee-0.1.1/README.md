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

Working on this. I'm new to python packaging.

Currently, asciibee is pip installable, but it doesn't do anything when imported.

I'd also like to provide an entrypoint so that it can be run as a CLI tool.

## Usage

NOTE: Currently requires a clone of the repo.

The best way to learn how to use the app is via the help text:

`$ poetry run python -m asciibee.main --help`

The most simple command is passing in a path to an image file:

`$ poetry run python -m asciibee.main ~/Downloads/starrynight.png`

## Development

The build system and package manager is [poetry](https://python-poetry.org/).

The easiest way to run the app locally:

`$ poetry run python -m asciibee.main <path_to_image>`

You can also install the deps and run it without the `poetry run` prefix.
