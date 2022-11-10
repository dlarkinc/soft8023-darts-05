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
#t.set_daemon(True)
t.start()
t.join()
print("Main program ending now")
