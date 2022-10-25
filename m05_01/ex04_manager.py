import sys
from multiprocessing import Process, current_process, Manager
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(val: Manager):
    name = current_process().name
    logger.debug(f"Start {name}")
    val[name] = current_process().pid
    logger.debug(f"Done {name}")
    sys.exit(0)


if __name__ == '__main__':
    with Manager() as manager:
        m = manager.dict()
        process = []
        for i in range(3):
            pr = Process(target=worker, args=(m, ))
            pr.start()
            process.append(pr)

        [pr.join() for pr in process]
        [print(pr.exitcode) for pr in process]
        print(m)

    logger.debug("End program")
