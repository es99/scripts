#!/usr/bin/python
#   coding: utf-8

import socket

target_host = "uol.com.br"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
client.send('GET / HTTP/1.1\r\nHost: uol.com.br\r\n')
response = client.recv(4096)

print(response)
