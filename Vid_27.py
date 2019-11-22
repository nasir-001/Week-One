#Authur Nasir Lawal
#Date: 22-Nov-2019

"""
Description: Tutorial on how to build a "web crawler"
"""

import requests

from bs4 import BeautifulSoup

def trade_spider(max_pages):
	page = 1
	while page <= max_pages:
		url = 'http://ww25.buckysroom.org/trade/search.php?r=&gc=pid-bodis-gcontrol118&query=Hotel&afdToken=3B1g5EaBFqyRzH3SwvTMfVDZjMRa0WkUMdZqrX95ajiY-_jsj88ZEee_ocFssudEY3LZg12oXib03PQIyu59iju1_s8LVImAWqQYyxLFEw?page=' + str(page)
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, features='html.parser')
		for link in soup.findAll('a', {'class': 'test_titleLink d_ g_'}):
			href = 'https://buckysroom.org' + link.get('href')
			title = link.string
			print(href)
			print(title)
		page += 1

trade_spider(1)