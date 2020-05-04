# port_scanner.py

import multiprocessing as mp
import socket
import datetime
import time
from local_machine_info import print_machine_info

exitFlag = 0

def check_port(data):
    addr, port = data
    print("Skeniram port: ", port, flush=True)
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((addr, port))
    if result == 0:
        print("Port %s je otvoren" % port, flush=True)
    sock.close()

def main():
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
    print("Broj coreova u ovom racunalu je %s, a koristit cemo %s procesa" % (mp.cpu_count(), mp.cpu_count() * 2))
    print("--------------------------------------------------------------")

    port_range = range(start_port, end_port+1)
    data = []
    for port in port_range:
        data.append((addr, port))

    start_time = time.time()

    pool = mp.Pool(mp.cpu_count() * 2)
    result = pool.map(check_port, data)

    print("Skeniranje portova zavrseno!!!")
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    print("Vrijeme pokretanja programa:")
    print(datetime.datetime.now())
    print("Program se izvodi na racunalu:")
    print_machine_info()
    print("--------------------------------------------------------------")
    main()