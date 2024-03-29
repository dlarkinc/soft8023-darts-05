import concurrent.futures
import threading
import time


def my_function(message, wait=2):
    print(threading.currentThread().getName() + " starting")
    time.sleep(wait)
    print(message)
    time.sleep(wait)
    print(threading.currentThread().getName() + " ended")
    return "goodbye!"


def my_callback(dummy):
    print("Some work to do after")


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        future1 = executor.submit(my_function, message="Hello", wait=6)
        #future1.add_done_callback(my_callback)
        time.sleep(1)
        future2 = executor.submit(my_function, message="there", wait=5)
        time.sleep(1)
        future3 = executor.submit(my_function, message="Dolly", wait=4)
        future4 = executor.submit(my_function, message="Parton")
        #print(future1.result(3))  # wait 5 seconds before timing out
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print(future4.result())
