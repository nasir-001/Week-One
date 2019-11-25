# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: tutorial on how to "paste image"
"""

from PIL import Image

faisal = Image.open("Faisal.jpg")
draw_2 = Image.open("Draw_2.jpg")

area = (100, 100, 300, 300)

faisal.paste(draw_2, area)

sister.show()