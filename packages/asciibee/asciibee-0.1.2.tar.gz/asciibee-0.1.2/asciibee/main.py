import argparse

from asciibee import constants, image

parser = argparse.ArgumentParser(
    prog="asciibee",
    description="""Convert an image to ASCII art

    The default settings are tuned to work well with fine art. Play with
    different shaders, image squaring, and value inversion for different
    results.

    Scaling is done by reducing the image by a factor of 2 until it fits in the
    terminal window or the width is below the max width you specify.

    Each ASCII character is chosen by expanding the range of pixel values to the
    full range of characters. For example, if the darkest value in the original
    image is 100 (of 255), and the lightest 230 (of 255), then 100 becomes the
    "new" 0 (and darkest char) and 230 the new 255 (and lightest char). You can
    provide the -1 flag to use exact values instead.""",
    formatter_class=argparse.RawTextHelpFormatter,
)
parser.add_argument("image_path", help="Path to the image to convert")
parser.add_argument(
    "-s",
    "--shader",
    help=f"The shader to use (they increase in complexity), default {constants.DEFAULT_SHADER}",
    type=int,
    choices=range(1, len(constants.SHADERS) + 1),
    default=constants.DEFAULT_SHADER,
    required=False,
)
parser.add_argument(
    "-S",
    "--user-shader",
    help="Define your own shader as a sequence of characters",
    required=False,
)
parser.add_argument(
    "-w",
    "--max-width",
    help="The maximum allowable output width (number of columns)",
    type=int,
    required=False,
)
parser.add_argument(
    "-i",
    "--invert-values",
    help="Invert the value scale (i.e. darker values will use heavier characters)",
    action="store_true",
)
parser.add_argument(
    "-1",
    "--one-to-one",
    help="Assign characters to the exact pixel value (do not normalize the value range)",
    action="store_true",
)
parser.add_argument(
    "-q",
    "--no-squaring",
    help="Do not add blank characters to help square the image (most fonts are taller than wide)",
    action="store_true",
)
parser.add_argument(
    "-O",
    "--original-size",
    help="Output the original size of the image (will override max-dimension)",
    action="store_true",
)

args = parser.parse_args()

def main():
    ascii_image = image.AsciiImage(
        args.image_path,
        shader=constants.SHADERS[args.shader - 1],
        user_shader=args.user_shader,
        max_allowable_width=args.max_width,
    )
    ascii_image.convert(
        args.original_size,
        args.invert_values,
        args.one_to_one,
        args.no_squaring,
    )
    ascii_image.show()

if __name__ == "__main__":
    main()
