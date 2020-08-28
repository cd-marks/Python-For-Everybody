# Write a program similar to urllink2.py which uses urllib to: 
#   - Read HTML from a data file, final all the <span> tags, extract the numbers from those tags and sum those numbers
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

num_sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Extract the content of the <span> tag, convert it to an integer and sum up the values
    num = int(tag.contents[0])
    num_sum = num_sum + num

print (num_sum)