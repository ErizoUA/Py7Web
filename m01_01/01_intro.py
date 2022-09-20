class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value


m = MyClass(20)
print(m.method())
print(m.__dict__)


def __init__(self, value):
    self.value = value


def method(self):
    return self.value


NewClass = type('NewClass', (object,), {'__init__': __init__, 'method': method})

m = NewClass(20)
print(m.method())
print(m.__dict__)
