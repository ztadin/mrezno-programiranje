import multiprocessing as mp
import random
import datetime
from local_machine_info import print_machine_info

def my_func(x):
    print(x**x)

def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(my_func, [4, 2, 3])

if __name__ == "__main__":
    print("Vrijeme pokretanja programa:")
    print(datetime.datetime.now())
    print("Program se izvodi na racunalu:")
    print_machine_info()
    print("--------------------------------------------------------------")
    main()

    