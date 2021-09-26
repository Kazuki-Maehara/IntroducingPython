from multiprocessing import Process, Queue
import time


def f(q):
    for i in range(2):
        print(q.get())


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    q.put([42, None, 'hello'])
    time.sleep(0.9)
    q.put([9, None, 'goodbye'])
    p.join()
    print('processes are done')
