def allowed_dating_age(my_age):
	girls_age = my_age / 2 + 7
	return girls_age

buckys_limit = allowed_dating_age(27)
creepy_joe_limit = allowed_dating_age(49)
print("Buckys can date", buckys_limit, "or order")
print("Creepy Joe can date girls", creepy_joe_limit, "or order")