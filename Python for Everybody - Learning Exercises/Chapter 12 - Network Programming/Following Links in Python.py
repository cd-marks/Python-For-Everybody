# Write a program which expands on urllinks.py. The program will use urllib to:
#   - Read HTML from a data file, extract the href= values from the anchor tags...
#   - Scan for a tag that is in a particular position relative to the first name in the list...
#   - Follow that link and repeat the process until you find the last name.
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

position = int(input('Enter the position of the link you want to follow: '))
num_of_reps = int(input('Enter the number of times you want this process to execute: '))
count = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the URL address of an HTML file: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
while num_of_reps > 0:
    for tag in tags:
        count += 1
        if count == position:
            url = tag.get('href', None)
            html = urllib.request.urlopen(url, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            print('Retrieving: ' + url)
    count = 0
    num_of_reps = num_of_reps - 1


