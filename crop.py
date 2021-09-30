import ipdb
import os
import sys
from PIL import Image

if len(sys.argv) != 2:
    print("Image param is require for this script")
    sys.exit()

img_name = sys.argv[1]
img = Image.open(img_name)
image_path = os.path.join(os.getcwd(), f'{img.filename}_croped')
os.makedirs(image_path, exist_ok=True)

total_crop = (img.size[0] * img.size[1]) / (200*200)
img_size = img.size

# first tile
x_start = 0
y_start = 0
x_end = 200
y_end = 200


def crop_image(x_start, y_start, x_end, y_end, count=1):
    if y_start == img_size[1]:
        return

    img_croped = img.crop((x_start, y_start, x_end, y_end))
    img_croped.save(f'{image_path}/img_{count}.jpg')
    saved = True

    if x_end == img_size[0]:
        x_start = 0
        x_end = 200
        y_start = y_start + 200 if y_start + 200 < img_size[1] else img_size[1]
        y_end = y_end + 200 if y_end + 200 < img_size[1] else img_size[1]
        saved = False

    if saved:
        # get next tile
        x_start = x_start + 200
        x_end = x_end + 200 if x_end + 200 < img_size[0] else img_size[0]

    count = count + 1
    return crop_image(x_start, y_start, x_end, y_end, count)


crop_image(x_start, y_start, x_end, y_end)
