#Authur: Nsair Lawal
#Date: 22-Nov-2019

"""
Description: Tutorial on how to use "unlimted argument"
"""

def add_number(*args):
	total = 0
	for a in args:
		total += a
	print(total)

add_number(3)
add_number(3, 32)
add_number(3, 43, 5453, 35434, 56)