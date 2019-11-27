# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Tutorial on how to use "Merge pillow"
"""

from PIL import Image

Faisal = Image.open("Faisal.jpg")
Draw = Image.open("Draw_4.jpg")

r1, g1, b1 = Faisal.split()
r2, g2, b2 = Draw.split()

new_img = Image.merge("RGB", (r2, g1, b2))

new_img.show()