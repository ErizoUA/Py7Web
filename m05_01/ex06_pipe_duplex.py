import sys
from multiprocessing import Process, current_process, Pipe
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f"Start {name}")
    while True:
        try:
            val = pipe.recv()
            logger.debug(f"Done {val}")
            pipe.send(f"Hello {val}")
        except EOFError:
            return None


def master(pipe: Pipe, store_: list):
    for el in store_:
        pipe.send(el)
        result = pipe.recv()
        print(result)


if __name__ == '__main__':
    recipient, sender = Pipe()
    store = ["Pavel", "Denys", "Nickita", "Yuri"]

    w = Process(target=worker, args=(recipient,))
    m = Process(target=master, args=(sender, store))

    w.start()
    m.start()

    m.join()
    recipient.close()
    sender.close()

    logger.debug("End program")
