from multiprocessing.managers import BaseManager

BaseManager.register('get_queue')
manager = BaseManager(address=('127.0.0.1', 5000), authkey=b'@#@32sdfd')

if __name__ == '__main__':
    manager.connect()
    queue = manager.get_queue()

    while True:
        if not queue.empty():
            print(queue.get())
