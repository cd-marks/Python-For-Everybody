# Write a program similar to json2.py to perform the following:
#   - Prompt the user for a URL, read the JSON data from that USL using urllib...
#   - Parse & extract the comment counts from the JSON data, and compute the sum of the numbers in the file.

import urllib.request, urllib.parse, urllib.error
import json

count = 0
num_sum = 0

while True:
    url = input('Enter a URL which locates a JSON file: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    js = json.loads(data)
    
    results = js['comments']
    for item in results:
        num = int(item['count'])
        count += 1
        num_sum += num

    print('Count: ' + str(count))
    print('Sum: ' + str(num_sum))
    exit()