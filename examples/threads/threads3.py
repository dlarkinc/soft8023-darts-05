import threading
import time


def my_function1(message):
    print(threading.currentThread().getName() + " starting")
    time.sleep(2)
    print(message)
    time.sleep(1)
    print(threading.currentThread().getName() + " ended")


def my_function2(message):
    print(threading.currentThread().getName() + " starting")
    time.sleep(1.5)
    print(message)
    time.sleep(3)
    print(threading.currentThread().getName() + " ended")


def my_function3(message):
    print(threading.currentThread().getName() + " starting")
    time.sleep(0.5)
    print(message)
    time.sleep(4)
    print(threading.currentThread().getName() + " ended")


v = "hello"

t0 = threading.Thread(target=my_function1, args=(v,))
t1 = threading.Thread(target=my_function2, args=(v,))
t2 = threading.Thread(target=my_function3, args=(v,))
t0.setDaemon(True)
t0.start()
t1.start()
t2.start()
t0.join()
t1.join()
print("done with 0 amd 1, waiting for 2")
t2.join()
print("Main program ending now")
