# Change Exercise 12.1 so that it counts the number of characters it has received and stops displaying any text after it has shown 300 characters.
#   - The program should retrieve the entire document, count the total number of characters and display the count of the number of characters at the end

import socket

count = 0
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url_input = input('Enter a URL address (http://.../) containing a file you want to read: ')
input_split = url_input.split('/')
try:
    host_domain = input_split[2]
except:
    print('Error: Invalid or non-existent URL')
    exit()

mysock.connect((host_domain, 80))
cmd = 'GET ' + url_input + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(500)
    if len(data) < 1 | count >= 3000:
        break
    count = count + len(data)
    print(data.decode()[0:3000],end='')

mysock.close()
print('\n' + '\n' + 'The number of printed characters is ' + str(count))