# echo_server.py

import socket
from _thread import *
import threading
import datetime
from local_machine_info import print_machine_info

def threaded(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data: continue
        if data.decode() == "zeljko_tadin":
            conn.sendall("Taj unos nije podrzan".encode())
            continue
        if data.decode() == "exit":
            print("Odspojen: ", addr[0], ":", addr[1])
            break
        conn.sendall(data)
    conn.close()


def main():
    print(datetime.datetime.now())
    print_machine_info()
    host = socket.gethostname()
    port = 12345
    echo_server = socket.socket()
    echo_server.bind((host, port))
    echo_server.listen(5)
    print("Cekam klijenta...")
    while True:
        conn, addr = echo_server.accept()
        print("Spojen: ", addr[0], ":", addr[1])
        start_new_thread(threaded, (conn, addr))
    echo_server.close()

if __name__ == '__main__':
    main()