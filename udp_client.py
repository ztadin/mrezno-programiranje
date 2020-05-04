# udp_client.py

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 2222

client_socket.sendto("Message from client".encode(), (host, port))
data, addr = client_socket.recvfrom(1024)
print(data)

client_socket.close()