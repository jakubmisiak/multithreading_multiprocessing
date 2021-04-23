from threading import *
from sigma import sigma 


def one_thread():
    one_thread=Thread(target=sigma)
    one_thread.start()
    one_thread.join()

def multi_threading():
    threads = [
        Thread(target=sigma),
        Thread(target=sigma),
        Thread(target=sigma),
        Thread(target=sigma),
    ]

    for i in threads:
        i.start()

    for i in threads:
        i.join()



