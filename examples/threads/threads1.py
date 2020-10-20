import threading
import time


def my_function(message):
    print(threading.currentThread().getName() + " starting")
    time.sleep(2)
    print(message)
    time.sleep(2)
    print(threading.currentThread().getName() + " ended")


v = "hello"

t = threading.Thread(target=my_function, args=(v,))
t.start()

while True:
    time.sleep(0.5)
    if t.isAlive():
        print(t.getName() + " is still active")
    else:
        print(t.getName() + " is not active")
        break
