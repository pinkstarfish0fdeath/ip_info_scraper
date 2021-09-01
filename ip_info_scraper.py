#!/usr/bin/env python3

# Easy recon tool that will pull data from ipinfo.io, disply it to stdout and save it to a CSV file.

# Program loop for user input that makes sure the AS number is integers only.
def input_loop():

    while True:
        as_number = input("AS number you want to target:")
        try:
            verify = int(as_number)
        except ValueError:
            # Loop continues until valid intergers are given
            print("Error! Please use the number only.")
        else:
            print("AS",as_number," is valid... Collecting data.")
            return as_number

import requests
from bs4 import BeautifulSoup
import sys

as_number = input_loop()
url = 'https://ipinfo.io/AS%s'%as_number
print(f"getting contents from {url}")

user_agent = {'User-agent': 'Mozilla/5.0'}
response  = requests.get(url, headers = user_agent)
html = response.content

# Make soup
soup = BeautifulSoup(html, 'html.parser')
container = soup.find(id="ipv4-data")
links = container.findAll('a')

for i,a in enumerate(links):
    if "Show" not in a.contents[0]:
        d = ''
        if (i > 0):
            d = ','
        print(f'{d}{a.contents[0]}', end='')