import logging
from functools import wraps, partial


def logged(func=None, *_, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    log_name = name if name else func.__module__
    log_message = message if message else func.__name__
    logger = logging.getLogger(log_name)
    logging.basicConfig(level=level)

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(level, log_message)
        return result
    return wrapper


@logged  # @logged
def add(x, y):
    return x + y


@logged(level=logging.ERROR, name='greeting')
def prefix_name(name):
    return f'Mr.(s) {name}'


if __name__ == '__main__':
    add(1, 1)
    prefix_name('Vasyl')

