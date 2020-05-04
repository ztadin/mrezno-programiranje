# port_scanner.py

import socket
import datetime
import time
from local_machine_info import print_machine_info

print("Vrijeme pokretanja programa:")
print(datetime.datetime.now())
print("Program se izvodi na racunalu:")
print_machine_info()
print("--------------------------------------------------------------")
print("Unesite adresu hosta koju zelite testirati:")
remote_host = input()
try:
    addr = socket.gethostbyname(remote_host)
except:
    print("Neispravna adresa hosta")
    exit()
print("Skeniram host %s, IP adresu: %s" % (remote_host, addr))

print("Unesite od kojeg do kojeg porta zelite napraviti skeniranje:")
start_port = int(input("Pocetni port >> "))
end_port = int(input("Zavrsni port >> "))
print("--------------------------------------------------------------")

start_time = time.time()
for port in range(start_port, end_port+1):
    print("Skeniram port: ", port)
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((addr, port))
    if result == 0:
        print("Port %s je otvoren" % port)
    sock.close()

print("Skeniranje portova zavrseno!!!")
print("--- %s seconds ---" % (time.time() - start_time))