from multiprocessing import Queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


queue = Queue()


def get():
    return queue


QueueManager.register('get_queue', callable=get)


if __name__ == '__main__':
    manager = QueueManager(address=('', 5000), authkey=b'@#@32sdfd')
    server = manager.get_server()
    print('Start server on port 5000')
    server.serve_forever()
