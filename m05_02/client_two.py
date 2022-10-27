from multiprocessing import Queue, Process
from multiprocessing.managers import BaseManager


def worker(queue: Queue, message: str):
    queue.put(message)


BaseManager.register('get_queue')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'@#@32sdfd')

if __name__ == '__main__':
    manager.connect()
    queue = manager.get_queue()
    for i in range(11):
        wrk = Process(target=worker, args=(queue, f"Spam message #{i} buy fignyu!"))
        wrk.start()
        wrk.join()
