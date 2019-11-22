#Authur: Nasir Lawal
#Date: 21-Nov-2019

"""
Description: Tutorial on how to unpack argument
"""

def health_calculator(age, apples_ate, cigs_smoked): # function for the calculator
	answer = (100-age) + (apples_ate * 3.5) - (cigs_smoked * 2) # variable named answer and the computation value
	print(answer) # print the variable 

buckys_data = [27, 20, 0] # list of the arguments

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2]) # calling the function one by one through their index
health_calculator(*buckys_data) # calling the index by unpacking the argument
