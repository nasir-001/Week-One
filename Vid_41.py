# Authur: Nasir Lawal
# Date: 23-Nov-2019

"""
Description: Tutorial how to use "Min, Max, Sort"
"""

stocks = {
	'GOOG': 520.54,
	'FB': 76.45,
	'YHOO': 39.28,
	'AMZN': 306,
	'APPL': 99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

