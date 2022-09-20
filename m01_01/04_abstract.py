from abc import ABCMeta, abstractmethod


class BazABC(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        ...

    @name.setter
    @abstractmethod
    def name(self):
        ...

    @staticmethod
    @abstractmethod
    def method():
        ...


# baz = BazABC()

class Baz(BazABC):
    @property
    def name(self):
        print('name')

    @name.setter
    def name(self):
        print('name setter')

    @staticmethod
    def method():
        print('Class Baz')


baz = Baz()
