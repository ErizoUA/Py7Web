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
    with open('result.txt', 'w') as fd:
        fd.write(str(result))


if __name__ == '__main__':
    print(f'CPU: {cpu_count()}')
    with Pool(cpu_count()) as p:
        p.map_async(worker, [el for el in range(30)], callback=cb)
        p.close()  # p.terminate()
        p.join()
    logger.debug("End program")

