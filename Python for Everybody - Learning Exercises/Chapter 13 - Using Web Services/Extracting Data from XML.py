# Write a program similar to geoxml.py. The program will:
#   - Prompt the user for a URL, read XML data from that URL using urllib...
#   - Parse & extract the comment counts from the XML data, and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

count = 0
num_sum = 0

while True:
    url = input('Enter a URL which locates an XML file: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)

    results = tree.findall('.//count')
    for item in results:
        num = int(item.text)
        count += 1
        num_sum += num

    print('Count: ' + str(count))
    print('Sum: ' + str(num_sum))
    exit()
