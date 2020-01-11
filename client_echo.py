#Cliente utilizado para se comunicar com o servidor

import socket

HOST = '127.0.0.1'
PORT = 65432

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect((HOST, PORT))

cliente.sendall(b'ola mundo')

resposta = cliente.recv(1024)

print(resposta)