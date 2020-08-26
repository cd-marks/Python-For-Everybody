# Change an existing socket program (socket1.py) to prompt the user to enter a URL so it can read any web page.
#   - You can use split('/') to break the URL into its component parts to you can extract the host name for a socket connect call.
#   - Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

url_input = input('Enter a URL address (http://.../): ')
input_split = url_input.split('/')
host_domain = input_split[2]

try: 
    mysock.connect((host_domain, 80))
except:
    print('Error: Invalid or non-existent URL')

cmd = 'GET ' + url_input + ' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
