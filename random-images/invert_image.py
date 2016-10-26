#!/bin/bash

from PIL import Image
import PIL.ImageOps
from sys import argv
image = Image.open(argv[1])
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save(argv[2])
