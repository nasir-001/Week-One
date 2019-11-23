# Authur: Nasir Lawal
# Date: 23-Nov-2019

"""
Description: Tutorial on the difference between "Syntax and Exception"
"""
while True:
	try:
		number = int(input("What is your fav number?\n"))
		print(18/number)
		break
	except ValueError:
		print("Make sure you enter a number")
	except ZeroDivisionError:
		print("Don't pick zero")
	except:
		break
	finally: 
		print("loop complete")
