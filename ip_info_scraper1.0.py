#!/usr/bin/python

import urllib
import urllib2
from bs4 import BeautifulSoup
import requests

url = ("https://ipinfo.io/target")
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
table = soup.find('table', id="block-table")

for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        print cell.text.replace('a-z','')
