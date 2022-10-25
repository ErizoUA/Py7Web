import sys
from multiprocessing import Process, current_process, Value, RLock
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(val: Value):
    logger.debug(f"Start {current_process().name}")
    with val.get_lock():
        val.value += 1
        logger.debug(f"Done {current_process().name}: {val.value}")
    sys.exit(0)


if __name__ == '__main__':
    lock = RLock()
    value = Value('d', 1, lock=lock)  # value = 1
    process = []
    for i in range(3):
        pr = Process(target=worker, args=(value, ))
        pr.start()
        process.append(pr)

    [pr.join() for pr in process]
    [print(pr.exitcode) for pr in process]
    print(value.value)
    logger.debug("End program")
