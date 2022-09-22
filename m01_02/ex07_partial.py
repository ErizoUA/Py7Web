from functools import partial


def add(x, y):
    return x + y


def part(x):
    def _add10(y):
        return x + y
    return _add10


test_add10 = part(10)

add10 = partial(add, y=10)
sum2plus2 = partial(add, 2, 2)


print(add10(3))  # add(3, 10)
print(sum2plus2())
print(test_add10 (3))