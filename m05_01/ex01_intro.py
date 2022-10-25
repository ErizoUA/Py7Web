from multiprocessing import Process
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args

    def run(self):
        logger.debug(f"In my process: {self.args}")


def worker(params):
    sleep(0.5)
    logger.debug(params)


if __name__ == '__main__':
    process = []
    for i in range(3):
        pr = Process(target=worker, args=(f'Count process of function - {i}', ))
        pr.start()
        process.append(pr)

    for i in range(3):
        pr = MyProcess(args=(f'Count process of class - {i}', ))
        pr.start()
        process.append(pr)

    [pr.join() for pr in process]
    [print(pr.exitcode) for pr in process]
    logger.debug("End program")
