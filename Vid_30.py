#Authur: Nasir Lawal
#Date: 23-Nov-2019

"""
Description: Tutorial how to use "classes"
"""

class Girl:

	gender = 'female'

	def __init__(self, name):
		self.name = name

r = Girl('Racheal')
s = Girl("Stanky")
print(r.gender +' '+ r.name)
print(s.gender +' '+ s.name)