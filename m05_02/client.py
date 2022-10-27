from multiprocessing import Queue, Process
from multiprocessing.managers import BaseManager


class Worker(Process):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        self.queue.put('Hello world!')


BaseManager.register('get_queue')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'@#@32sdfd')

if __name__ == '__main__':
    manager.connect()
    queue = manager.get_queue()
    wrk = Worker(queue)
    wrk.start()
    wrk.join()