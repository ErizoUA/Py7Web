
class Calculate:
    def __init__(self, x):
        self.x = x

    def add(self, y):
        self.x = self.x + y
        return self.x


def sub(self, y):
    self.x = self.x - y
    return self.x


if __name__ == '__main__':
    c = Calculate(10)
    c.add(3)
    c_sub = sub.__get__(c, Calculate)
    print(c.x)
    c_sub(5)
    print(c.x)
