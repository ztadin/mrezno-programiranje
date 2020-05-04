# tcp_client_google.py

import socket

client_socket = socket.socket()
remote_host = "www.google.com"
host = socket.gethostbyname(remote_host)
port = 80

print("IP for hostname %s is: %s" % (remote_host, host))
client_socket.connect((host, port))
print("The socket has successfully connected to Google on port == %s, and IP address == %s" % (port, host))
client_socket.close()