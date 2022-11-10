import threading
import time


def my_function(message):
    print(threading.current_thread().getName() + " starting")
    time.sleep(2)
    print(message)
    time.sleep(2)
    print(threading.current_thread().getName() + " ended")


v = "hello"

t = threading.Thread(target=my_function, args=(v,))
t.start()

while True:
    time.sleep(0.5)
    if t.is_alive():
        print(t.getName() + " is still active")
    else:
        print(t.getName() + " is not active")
        break
