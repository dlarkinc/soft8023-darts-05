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
t.setDaemon(True)
t.start()
#t.join()
print("Main program ending now")
