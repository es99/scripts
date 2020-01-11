#implementação de um servidor socket simples, que ecoará o que receber de volta ao cliente.

import socket

IP = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((IP, PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Conectado por: ', addr)
		while True:
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)