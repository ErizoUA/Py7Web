class CountingClass:
    instance_created = 0

    def __new__(cls, *args, **kwargs):
        print(f'{cls} __new__ CountingClass called')
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created = cls.instance_created + 1
        return instance if instance.number == 2 else None

    def __init__(self, value):
        print(f'{self}, __init__ CountingClass called')
        self.value = value


if __name__ == '__main__':
    print('Створення екземпляру класу')
    instance_01 = CountingClass(20)
    print(instance_01)
    print('--------------------------------')
    instance_02 = CountingClass(20)
    print(instance_02)
    print('--------------------------------')
    instance_03 = CountingClass(20)
    print(instance_03)
    print('--------------------------------')
    print(CountingClass.instance_created)
