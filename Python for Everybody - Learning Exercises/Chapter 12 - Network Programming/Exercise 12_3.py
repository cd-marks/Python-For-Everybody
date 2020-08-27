# Use urllib to replicate the functionality of Exercise 12.2
#   - Retrieve a document from a URL, display up to 3,000 characters and display a count of the number of characters
#   - Don't worry about the headers for this exercise

import urllib.request, urllib.parse, urllib.error

count = 0
url_input = input('Enter a URL address (http://.../) containing a file you want to read: ')

try:
    fhand = urllib.request.urlopen(url_input)
except:
    print('Error: Invalid or non-existant URL')
    exit()

data = fhand.read(3000).decode()
count = len(data)

print(data + '\n' + '\n' + 'The number of printed characters is ' + str(count))
