import sys
from multiprocessing import Process, current_process, Queue
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

q = Queue()


def worker(queue: Queue):
    name = current_process().name
    logger.debug(f"Start {name}")
    val = queue.get()
    logger.debug(f"Done {val}")
    sys.exit(0)


if __name__ == '__main__':

    w1 = Process(target=worker, args=(q,))
    w2 = Process(target=worker, args=(q, ))

    w1.start()
    w2.start()

    q.put(42)
    sleep(1)
    q.put(10)

    logger.debug("End program")
