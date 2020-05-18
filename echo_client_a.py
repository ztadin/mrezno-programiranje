# echo_client_a.py

import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345

print(datetime.datetime.now())
print_machine_info()

client_socket = socket.socket()
client_socket.connect((host, port))

while True:
    print ("Unesite tekst za slanje serveru (exit za kraj)")
    message = input()

    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)

    if message == "exit":
        break

    print(str(data.decode('ascii')))
    
client_socket.close()