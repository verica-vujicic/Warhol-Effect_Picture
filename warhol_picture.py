"""
The program takes one image 
and creates the path of 6 
copies (2 rows, 3 columns)
"""

# Pillow package have to installed
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'simba-sq.jpg'

def main():
    image = SimpleImage(PATCH_NAME)
    new_image = final_image()
    new_image.show()
    image.show()

def final_image():
    new_image = SimpleImage.blank(WIDTH, HEIGHT)
    # This is an example which should generate a pinkish patch
    patch1 = make_recolored_patch(1.5, 0, 1.5) #this is pink Simba
    patch2 = make_recolored_patch(0, 1.5, 1.5) # this is green Simba
    patch1_width = patch1.width
    patch1_height = patch1.height
    patch2_width = patch1.width
    patch2_height = patch2.height
    for y in range(patch1_height):
        for x in range(patch1_width):
            pixel1 = patch1.get_pixel(x, y)
            pixel2 = patch2.get_pixel(x, y)
            new_image.set_pixel(x, y, pixel1)
            new_image.set_pixel(patch2_width + x, y, pixel2)
            new_image.set_pixel(patch1_width * 2 + x, y, pixel1)
            new_image.set_pixel(x, patch2_height + y, pixel2)
            new_image.set_pixel(patch1_width + x, patch1_height + y, pixel1)
            new_image.set_pixel(patch2_width * 2 + x, patch2_height + y, pixel2)
    return new_image

if __name__ == '__main__':
    main()
