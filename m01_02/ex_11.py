import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Calculate:
    def __init__(self, x):
        self.x = x

    @Profiled
    def add(self, y):
        self.x = self.x + y
        return self.x


if __name__ == '__main__':
    # add(2, 3)
    # add(3, 4)
    # print(f'add count called {add.counter}')

    c = Calculate(10)
    c.add(3)
    print(f'add count called {Calculate.add.counter}')
    