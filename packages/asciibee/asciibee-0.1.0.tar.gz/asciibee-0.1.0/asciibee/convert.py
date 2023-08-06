import os

import numpy
from PIL import Image


class AsciiImage:
    ascii_matrix: list = []

    def __init__(
        self,
        image_path: str,
        shader: list,
        user_shader: str = None,
        max_allowable_width: int = None,
    ) -> None:
        self.image_path = image_path
        self.shader = shader if not user_shader else user_shader
        self.max_allowable_width = max_allowable_width

    def _reduce(self, image: Image) -> Image:
        if not self.max_allowable_width:
            terminal_size = os.get_terminal_size()
            while image.size[0] > terminal_size[0] or image.size[1] > terminal_size[1]:
                image = image.reduce(2)
        else:
            while image.size[0] > self.max_allowable_width:
                image = image.reduce(2)
        return image

    def _rotate_and_flip(self, matrix: list) -> list:
        rotated = numpy.rot90(matrix, 3)
        return numpy.flip(rotated, 1)

    def convert(
        self,
        original_size: bool = False,
        invert_values: bool = False,
        one_to_one: bool = False,
        no_squaring: bool = False,
    ) -> None:
        with Image.open(self.image_path).convert("L") as image:
            if not original_size:
                image = self._reduce(image)

            if invert_values:
                self.shader = self.shader[::-1]

            spacer = "" if no_squaring else " "

            if one_to_one:
                for x in range(image.size[0]):
                    self.ascii_matrix.append([])
                    for y in range(image.size[1]):
                        pixel = image.getpixel((x, y))
                        value = (pixel * (len(self.shader))) / 255
                        self.ascii_matrix[x].append(self.shader[int(value) - 1] + spacer)
            else:
                darkest_value = image.getpixel((0, 0))
                lightest_value = image.getpixel((0, 0))
                for x in range(image.size[0]):
                    for y in range(image.size[1]):
                        darkest_value = min(darkest_value, image.getpixel((x, y)))
                        lightest_value = max(lightest_value, image.getpixel((x, y)))

                for x in range(image.size[0]):
                    self.ascii_matrix.append([])
                    for y in range(image.size[1]):
                        # What percentage of the full range is this pixel?
                        pixel = image.getpixel((x, y))
                        value = (pixel - darkest_value) / (lightest_value - darkest_value)
                        # What character should we use for this pixel?
                        char_index = int(value * (len(self.shader) - 1))
                        self.ascii_matrix[x].append(self.shader[char_index] + spacer)

        self.ascii_matrix = self._rotate_and_flip(self.ascii_matrix)

    def show(self) -> None:
        for row in self.ascii_matrix:
            for char in row:
                print(char, end="")
            print()
