# echo_client.py

import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345

print(datetime.datetime.now())
print_machine_info()
print ("Unesite tekst za slanje serveru")
message = input()

client_socket = socket.socket()

client_socket.connect((host, port))

client_socket.sendall(message.encode())

data = client_socket.recv(1024)

print(data)
client_socket.close()