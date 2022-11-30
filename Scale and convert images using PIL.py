#!/usr/bin/env python3
import os, sys
from PIL import Image


source_dir = "images/"
new_dir = "/opt/icons/"

for filename in os.listdir(source_dir):
    if filename != "*.tif":
        im = Image.open(os.path.join(source_dir, filename))
        im = im.rotate(-90)
        im = im.resize((128,128))
        im = im.convert("RGB")
        im.save(os.path.join(new_dir, filename+".jpeg"))
