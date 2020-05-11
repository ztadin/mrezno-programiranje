# tcp_server.py

import socket
import ssl
import datetime
from local_machine_info import print_machine_info

print("Vrijeme pokretanja programa:")
print(datetime.datetime.now())
print("Program se izvodi na racunalu:")
print_machine_info()
print("--------------------------------------------------------------")

server_socket = socket.socket()
host = "localhost"
port = 10023

server_socket.bind((host, port))

print("Waiting for connection...")
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    connection_stream = ssl.wrap_socket(conn, server_side=True, certfile="localhost.pem")
    print('Got Connection from ', addr)
    connection_stream.send('Server Saying Hi'.encode())
    connection_stream.shutdown(socket.SHUT_RDWR)
    connection_stream.close()