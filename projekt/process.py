import multiprocessing
from sigma import sigma 


def four_processes():
    processes = [
        multiprocessing.Process(target=sigma),
        multiprocessing.Process(target=sigma),
        multiprocessing.Process(target=sigma),
        multiprocessing.Process(target=sigma),
    ]
    
    for i in processes:
        i.start()

    for i in processes:
        i.join()

def all_processes():
    cpus =  multiprocessing.cpu_count()
    processes = []
    for y in range(1, cpus+1):
        processes.append(multiprocessing.Process(target=sigma))

    for i in processes:
        i.start()

    for i in processes:
        i.join()

