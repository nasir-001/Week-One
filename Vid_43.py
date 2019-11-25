# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Tutorial on how to form an "image from another image"
"""

from PIL import Image

img = Image.open("Faisal.jpg")

area = (100, 100, 300, 300)
cropped_img = img.crop(area)

img.show()
cropped_img.show()