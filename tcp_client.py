# tcp_client.py

import socket
import ssl
import datetime
from local_machine_info import print_machine_info

print("Vrijeme pokretanja programa:")
print(datetime.datetime.now())
print("Program se izvodi na racunalu:")
print_machine_info()
print("--------------------------------------------------------------")

client_socket = socket.socket()
host = "localhost"
port = 10023

print(host)

ssl_client_socket = ssl.wrap_socket(client_socket, ca_certs="localhost.pem", cert_reqs=ssl.CERT_REQUIRED)

ssl_client_socket.connect((host, port))

print(ssl_client_socket.recv(1024))

ssl_client_socket.close()