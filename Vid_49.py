# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Tutorial on how to "breaking image using pillow"
"""

from PIL import Image

Faisal = Image.open('Faisal.jpg')

r, g, b = Faisal.split()

r.show()
g.show()
b.show()