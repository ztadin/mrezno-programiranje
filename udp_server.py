# udp_server.py

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 2222

server_socket.bind((host, port))

print("Waiting for client message...")
while True:
    data, addr = server_socket.recvfrom(1024)
    print('Got Message(%s) from %s' % (data, addr))
    server_socket.sendto('Server Saying Hi'.encode(), addr)
