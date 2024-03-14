import time
from threadin_g import Thread
from time import sleep


# counter = 0
#
#
# def increase(by):
#     global counter
#
#     l_counter = counter
#     l_counter += by
#
#     sleep(1)
#
#     counter = l_counter
#     print(f'{counter}')
#
#
# t1 = Thread(target=increase, args=(10,))
# t2 = Thread(target=increase, args=(20,))
#
# t1.start()
# t2.start()
from threadin_g import current_thread

# def get_data(data):
#     for i in range(10):
#         print(f'{data} {current_thread().name}')
#         sleep(1)
#
#
# def get_data_2(data):
#     for i in range(10):
#         print(f'{data} {current_thread().name}')
#         sleep(1)
#
#
# t1 = Thread(target=get_data, args=(str(time.time()),), name='Thr 1')
# t2 = Thread(target=get_data_2, args=(str(time.time()),), name='Thr 2')
#
# t1.start()
# t2.start()
#
# for i in range(10):
#     print('main thread')
#     sleep(2)
from threadin_g import Lock, RLock

# val = 0
# #locker = Lock()
# locker = RLock()
#
# def inc_val():
#     locker.acquire()
#     print('inc val 1')
#     sleep(2)
#     print('inc val 1')
#     locker.release()
#
#
# def inc_val2():
#     #locker.acquire()
#     print('inc val 2')
#     #locker.release()
#
#
# t1 = Thread(target=inc_val).start()
# t2 = Thread(target=inc_val2).start()
#
# print(time.strftime('%H:%M:%S'))


import time
from threadin_g import Thread, Semaphore
from time import sleep


# s = Semaphore(3)
#
# def tes_func(pl):
#     s.acquire()
#
#     print(pl)
#     sleep(2)
#     s.release()
#
#
# threads = [Thread(target=tes_func, args=(i,)) for i in range(8)]
#
# for i in threads:
#     i.start()

# from threading import Timer
#
#
# def inc_val():
#     while True:
#         print('Test func')
#         sleep(1)
#
# thr1 = Timer(15, inc_val).start()
#
# sleep(5)
#
# thr1.cancel()


# from threading import Barrier
#
# def func(barrier):
#     sleep(1)
#
#     print(f'Thread {current_thread().name} go on')
#
#     barrier.wait()
#
#     print(f'Thread {current_thread().name} go on barrier')
#
#
# bar = Barrier(5)
#
# for i in range(10):
#     Thread(target=func, args=(bar,), name=f'Tr-{i}').start()
#     sleep(1)

import time
from multiprocessing import Process, freeze_support


def tes_func():
    while True:
        print('Hello')
        sleep(1)


if __name__ == '__main__':
    #freeze_support()
    Process(target=tes_func, name='Prc1').start()
