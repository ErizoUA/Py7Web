import sys
from multiprocessing import Pool, current_process, cpu_count
import logging
from time import sleep

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def worker(val: int):
    name = current_process().name
    logger.debug(f"Start {name}")
    sleep(1)
    logger.debug(f"Done {val**2}")
    return val**2


def cb(result):
    print(result)


if __name__ == '__main__':
    print(f'CPU: {cpu_count()}')
    with Pool(cpu_count()) as p:
        for i in range(10):
            p.apply_async(worker, args=(i, ), callback=cb)
            # r = p.apply(worker, args=(i, ))
            # print(r)
        p.close()  # p.terminate()
        p.join()
    logger.debug("End program")

