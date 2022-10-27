from multiprocessing import Process, RLock as PrLock
from threading import Thread, RLock as ThLock
from multiprocessing.dummy import Pool, RLock as PlLock  # Thread
from time import time


def worker(values, filename, lock):
    with lock:
        with open(filename, 'a') as f:
            for num in values:
                f.write(f'{num ** 2}\n')


if __name__ == '__main__':
    values = list(range(6000000))

    th_lock = ThLock()
    thread_file = 'thread_squares.txt'
    threads = [
        Thread(target=worker, args=(values[:2000000], thread_file, th_lock)),
        Thread(target=worker, args=(values[2000000:4000000], thread_file, th_lock)),
        Thread(target=worker, args=(values[4000000:], thread_file, th_lock)),
    ]
    timer = time()
    [th.start() for th in threads]
    [th.join() for th in threads]
    print(f"Time for 3 threads: {round(time() - timer, 4)}")

    pr_lock = PrLock()
    process_file = 'process_squares.txt'
    processes = [
        Process(target=worker, args=(values[:2000000], process_file, pr_lock)),
        Process(target=worker, args=(values[2000000:4000000], process_file, pr_lock)),
        Process(target=worker, args=(values[4000000:], process_file, pr_lock)),
    ]

    timer = time()
    [pr.start() for pr in processes]
    [pr.join() for pr in processes]
    [pr.close() for pr in processes]
    print(f"Time for 3 process: {round(time() - timer, 4)}")

    pl_lock = PlLock()
    pool_file = "pool_squares.txt"
    timer = time()
    with Pool(3) as pool:
        pool.starmap(worker, [(values[:2000000], pool_file, pl_lock), (values[2000000:4000000], pool_file, pl_lock),
                              (values[4000000:], pool_file, pl_lock)])
    print(f"Time for 3 pool: {round(time() - timer, 4)}")

    timer = time()
    worker(values, 'squares.txt', pr_lock)
    print(f"Time for 1 process: {round(time() - timer, 4)}")
