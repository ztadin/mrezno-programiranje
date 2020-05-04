# port_scanner.py

import queue
import threading
import socket
import datetime
import time
from local_machine_info import print_machine_info

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q
    def run(self):
        process(self.q)

def process(q):
    while not exitFlag:
        if not workQueue.empty():
            port = q.get()
            check_port(port)

def check_port(port):
    print("Skeniram port: ", port, flush=True)
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((addr, port))
    if result == 0:
        print("Port %s je otvoren" % port, flush=True)
    sock.close()

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

port_range = list(range(start_port, end_port+1))

start_time = time.time()

workQueue = queue.Queue(len(port_range))
for port in port_range:
    workQueue.put(port)

threads = []
for t in range(4):
    thread = myThread(workQueue)
    thread.start()
    threads.append(thread)

while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print("Skeniranje portova zavrseno!!!")
print("--- %s seconds ---" % (time.time() - start_time))