#Authur: Nasir Lawal
#Date: 21-Nov-2019

"""
Description: Tutorial on how to use a default argument
"""

def get_gender(sex='Unknown'):
	if sex is 'M':
		sex = "Male"
	elif sex = 'F':
		sex = "Female"
	print(sex)

get_gender('M')
get_gender('F')
get_gender()
	