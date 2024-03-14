import multiprocessing
import time
from multiprocessing import Process

def heavy(n):
    for x in range(1, n):
        for y in range(1, n):
            x**y

def sequent(n):
    for i in range(n):
        heavy(250)

    print(f'{n} cycles')


def processed(procs, calc):
    processes = []

    for pr in range(procs):
        proc = Process(target=sequent, args=(calc,))
        processes.append(proc)
        proc.start()

    for pr in processes:
        pr.join()


if __name__ == '__main__':

    start = time.time()
    n_proc = multiprocessing.cpu_count()
    print(n_proc)
    calc = 80 // n_proc

    processed(n_proc, calc)

    end = time.time()

    print('Total time:', end-start)
