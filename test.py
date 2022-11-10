import socket
import urllib.error

import requests
import urllib.request as req

try:
    response = req.urlopen('https://www.python.org')
except urllib.error.URLError as e:
    if (isinstance(e.reason, socket.timeout)):
        print("Time Out")
# print(response.read().decode('utf-8'))

print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
