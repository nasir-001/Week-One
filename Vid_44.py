# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Tutorial on how to "Resize an image"
"""

from PIL import Image

draw_3 = Image.open("draw_3.jpg")
square_draw_3 = draw_3.resize((250, 250))

flip_draw_3 = draw_3.transpose(Image.FLIP_LEFT_RIGHT)

spin_draw_3 = draw_3.transpose(Image.ROTATE_90)

draw_3.show()
square_draw_3.show()
flip_draw_3.show()
spin_draw_3.show()