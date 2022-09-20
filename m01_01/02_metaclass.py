print('Визначення метакласу')


class OurMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):  # name -> __name__, base -> __base__, namespace -> __dict__
        print(f'{mcs} __new__ metaclass called')
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(f'{mcs} __prepare__ metaclass called')
        return super().__prepare__(name, bases, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(f'{cls} __call__ metaclass called')
        return super().__call__(*args, **kwargs)


print('Визначення класу')


class MyClass(metaclass=OurMeta):
    def __new__(cls, *args, **kwargs):
        print(f'{cls} __new__ MyClass called')
        return super().__new__(cls)

    def __init__(self, value):
        print(f'{self}, __init__ MyClass called')
        super().__init__()
        self.value = value


if __name__ == '__main__':
    print('Створення екземпляру класу')
    instance = MyClass(20)
    print(instance.value)
