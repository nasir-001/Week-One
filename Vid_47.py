# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Tutorial on how to convert image "mode to photo"
"""

from PIL import Image
from PIL import ImageFilter

draw_4 = Image.open('Faisal.jpg')

blur = draw_4.filter(ImageFilter.BLUR)
detail = draw_4.filter(ImageFilter.DETAIL)
edges = draw_4.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()