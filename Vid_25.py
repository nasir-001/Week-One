#Authur: Nasir Lawal
#Date: 23-Nov-2019

"""
Description: Tutorial how to download a "CSV File"
"""

from urllib import request

goog_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/snakes_count_10000.csv'

def download_stock_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split('\\n')
	dest_url = r'goog.csv'

	fx = open(dest_url, 'w')
	for line in lines:
		fx.write(line + "\n")
	fx.close()

download_stock_data(goog_url)