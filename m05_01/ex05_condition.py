from multiprocessing import Condition, Process
from time import sleep
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def master(con: Condition):
    logger.debug('Master work hard')
    with con:
        logger.debug('Работайте сонце ще високо!')
        con.notify_all()


def worker(con: Condition):
    logger.debug(f'waiting...')
    with con:
        con.wait()
        # some work
        logger.debug(f'finished')


if __name__ == '__main__':
    con = Condition()

    m = Process(target=master, args=(con, ))

    w1 = Process(target=worker, args=(con, ))
    w2 = Process(target=worker, args=(con, ))

    w1.start()
    w2.start()
    sleep(1)
    m.start()
