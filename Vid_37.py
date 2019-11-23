# Authur: Nasir Lawal
# Date: 23-Nov-2019

"""
Description: Tutorial how to use "pillow"
"""

from PIL import Image

img = Image.open("Draw_1.jpg")
print(img.size)
print(img.format)

img.show()