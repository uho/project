
import numpy
import os
from PIL import Image

IMAGE_SOURCE = 'images_30/'

PATH_ORIGINAL = IMAGE_SOURCE + 'thumbnails/'
PATH_BLURRED_03 = IMAGE_SOURCE + 'blurred_03/'
PATH_BLURRED_06 = IMAGE_SOURCE + 'blurred_06/'
PATH_BLURRED_09 = IMAGE_SOURCE + 'blurred_09/'
PATH_BLURRED_12 = IMAGE_SOURCE + 'blurred_12/'
PATH_BLURRED_15 = IMAGE_SOURCE + 'blurred_15/'
PATH_MOSAIC_05 = IMAGE_SOURCE + 'mosaic_05/'
PATH_MOSAIC_10 = IMAGE_SOURCE + 'mosaic_10/'
PATH_MOSAIC_15 = IMAGE_SOURCE + 'mosaic_15/'
PATH_MOSAIC_20 = IMAGE_SOURCE + 'mosaic_20/'
PATH_MOSAIC_25 = IMAGE_SOURCE + 'mosaic_25/'


def image_path_to_array(path):
    return numpy.array(Image.open(path)).flatten().tolist()


def read_images_from_directory(target=PATH_BLURRED_06):
    X = []
    y = []

    for filename in os.listdir(PATH_ORIGINAL):
        if filename.endswith('.ppm'):
            X.append(image_path_to_array(os.path.join(target, filename)))
            y.append(image_path_to_array(os.path.join(PATH_ORIGINAL, filename)))

    return X, y
