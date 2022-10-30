#!/usr/bin/python3
import os
from PIL import Image

dir_name = "images"
image_path = "modify"
size = (128,128)
# os.mkdir(image_path)
img_list = os.listdir(dir_name)
for img in img_list:
    full_img_name = os.path.join(dir_name,img)
    im = Image.open(full_img_name)
    new_im = im.rotate(270).resize(size)
    new_im.convert("RGB").save(f"{image_path}/{img}",format="JPEG")
    
    