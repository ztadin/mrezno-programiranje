# threading_primjer_threading_modul.py

import threading
import time
import datetime
from local_machine_info import print_machine_info

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Pokrecem nit ", self.name)
        print_time(self.name, self.counter, 5)
        print("Izlazim iz niti ", self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

print("Vrijeme pokretanja programa:")
print(datetime.datetime.now())
print("Program se izvodi na racunalu:")
print_machine_info()
print("--------------------------------------------------------------")

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

print("Izlazim iz glavne niti")
        