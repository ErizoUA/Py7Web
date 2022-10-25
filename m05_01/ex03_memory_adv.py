import sys
from multiprocessing import Process, current_process, Value, RLock, Array
from ctypes import c_double, Structure
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


class Point(Structure):
    _fields_ = [('x', c_double), ('y', c_double)]


def worker(val: Value, string: Array, arr: Array):
    logger.debug(f"Start {current_process().name}")
    with val.get_lock():
        val.value += 1
        logger.debug(f"Done {current_process().name}: {val.value}")
    with string.get_lock():
        string.value = string.value.upper()
    with arr.get_lock():
        for el in arr:
            el.x *= 10
            el.y *= 10

    sys.exit(0)


if __name__ == '__main__':
    lock = RLock()
    value = Value(c_double, 1.5, lock=lock)  # value = 1
    string = Array('c', b'Web group 7', lock=lock)
    arr = Array(Point, [(3, 4), (-4, 6), (0, 0)], lock=lock)

    process = []
    for i in range(3):
        pr = Process(target=worker, args=(value, string, arr))
        pr.start()
        process.append(pr)

    [pr.join() for pr in process]
    [print(pr.exitcode) for pr in process]
    print(value.value, string.value)
    print([(el.x, el.y) for el in arr])

    logger.debug("End program")
