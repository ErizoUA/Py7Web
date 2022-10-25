import sys
from multiprocessing import Process, current_process, Pipe
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

recipient1, sender1 = Pipe(duplex=False)
recipient2, sender2 = Pipe(duplex=False)


def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f"Start {name}")
    val = pipe.recv()
    logger.debug(f"Done {val ** 2}")
    sys.exit(0)


if __name__ == '__main__':
    pr1 = Process(target=worker, args=(recipient1,))
    pr1.start()
    pr2 = Process(target=worker, args=(recipient2,))
    pr2.start()
    sender1.send(4)
    sleep(1)
    sender2.send(5)
    logger.debug("End program")
