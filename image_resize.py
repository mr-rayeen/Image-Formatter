#!/usr/bin/python3

from PIL import Image

image = "1Inazuma-Eleven-Wallpaper-inazuma-eleven-.jpg"
im = Image.open(image)
print(im.format,im.size)
new_im = im.rotate(90).resize((128,128)).save("new-image.png")
new_im = Image.open("new-image.png")
print(new_im.format,new_im.size)