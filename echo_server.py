# echo_server.py

import socket
import datetime
from local_machine_info import print_machine_info

host = socket.gethostname()
port = 12345

echo_server = socket.socket()
echo_server.bind((host, port))
echo_server.listen(5)

print(datetime.datetime.now())
print_machine_info()
print("Cekam klijenta...")


while True:
    conn, addr = echo_server.accept()
    print("Spojen: ", addr)
    data = conn.recv(1024)
    if not data: continue
    if data.decode() == "zeljko_tadin":
        conn.sendall("Taj unos nije podrzan".encode())
        continue
    conn.sendall(data)
    conn.close()
