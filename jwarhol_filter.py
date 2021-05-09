"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 3
N_COLS = 3
PATCH_SIZE = 945
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
NUM_PATCHES = N_COLS * N_ROWS
PATCH_NAME = 'images/peri.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    for row in range(N_ROWS):
        for col in range(N_COLS):

            # Assign to a generated random integer between 1 & 6.
            randnum = col + row * N_COLS + 1

            # Print a random colored image.
            if randnum == 1:
                patch = make_recolored_patch(1.5, 0, 1.5)
            if randnum == 2:
                patch = make_recolored_patch(.5, 0, 1.5)
            if randnum == 3:
                patch = make_recolored_patch(1, 2, 0)
            if randnum == 4:
                patch = make_recolored_patch(.5, 1, .5)
            if randnum == 5:
                patch = make_recolored_patch(1, 0, 0)
            if randnum == 6:
                patch = make_recolored_patch(2, 0, 0)
            if randnum == 7:
                patch = make_recolored_patch(2, 1, .5)
            if randnum == 8:
                patch = make_recolored_patch(0, 0, 1.5)
            if randnum == 9:
                patch = make_recolored_patch(0, 0, 2)
            if randnum == 10:
                patch = make_recolored_patch(1.5, 1.5, 1.5)

            # Place all six patches on the final image.
            for y in range(PATCH_SIZE):
                for x in range(PATCH_SIZE):
                    pixel = patch.get_pixel(x, y)
                    final_image.set_pixel(x + PATCH_SIZE * col, y + PATCH_SIZE * row, pixel)

    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


if __name__ == '__main__':
    main()
