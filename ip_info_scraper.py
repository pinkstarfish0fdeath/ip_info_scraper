#!/usr/bin/env python3.7

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
            break

import requests
from bs4 import BeautifulSoup

as_number = input_loop()
url = ('https://ipinfo.io/AS', as_number,)
response = requests.get(url)
html = response.content

# Make soup
soup = BeautifulSoup(html)
table = soup.find('table', id="block-table")

# Print all the IP blocks from the target.
for row in table.find_all('tr'):
    for cell in row.find_all('td'):
        print (cell.text.replace('a-z',''))