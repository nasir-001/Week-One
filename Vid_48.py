# Authur: Nasir Lawal
# Date: 25-Nov-2019

"""
Description: Toturial on how to "Sort"
"""

from operator import itemgetter

users = [
	{'fname': 'Nasir', 'lname': 'Lawal'},
	{'fname': 'Tom', 'lname': 'Roberts'},
	{'fname': 'Jenna', 'lname': 'Zunks'},
	{'fname': 'Sally', 'lname': 'Jones'},
	{'fname': 'Amanda', 'lname': 'Roberts'},
	{'fname': 'Dean', 'lname': 'Hayes'},
	{'fname': 'Tom', 'lname': 'Jones'},
]

for x in sorted(users, key=itemgetter('fname')):
	print(x)

print('---------')

for x in sorted(users, key=itemgetter('fname', 'lname')):
	print(x)