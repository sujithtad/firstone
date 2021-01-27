#!/usr/bin/python3
import os
from PIL import Image

directory = "/home/student-02-e7c7d36f94e7/images"

for file in os.listdir(directory):
    im = Image.open("images/" + file)
    im_flipped = im.transpose(method=Image.ROTATE_270)
    im_flipped = im_flipped.resize((128, 128))
    im_flipped.save("/opt/icons/" + file + ".jpeg")
