# from https://realpython.com/intro-to-python-threading/#deadlock

import threading

l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.release()
l.acquire()
print("acquired lock twice")
