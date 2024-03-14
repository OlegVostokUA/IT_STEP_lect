import time
from threading import Thread

def heavy(n):
    for x in range(1, n):
        for y in range(1, n):
            x**y


def sequent(n):
    for i in range(n):
        heavy(250)

    print(f'{n} cycles')


def threaded(threads, calc):
    threads_ = []
    for t in range(threads):
        tr = Thread(target=sequent, args=(calc,))
        threads_.append(tr)
        tr.start()

    for t in threads_:
        t.join()

start = time.time()

threaded(4, 20)

end = time.time()

print('Total time:', end-start)
