import sys
from multiprocessing import Process, current_process, JoinableQueue
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

jq = JoinableQueue()


def worker(jqueue: JoinableQueue):
    name = current_process().name
    logger.debug(f"Start {name}")
    val = jqueue.get()

    logger.debug(f"Done {val**2}")
    jqueue.task_done()
    sys.exit(0)


if __name__ == '__main__':

    w1 = Process(target=worker, args=(jq,))
    w2 = Process(target=worker, args=(jq, ))

    w1.start()
    w2.start()

    jq.put(42)
    sleep(1)
    jq.put(10)
    jq.join()
    logger.debug("End program")
