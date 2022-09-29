import datetime


class Event:
    _observers = []
    # { 'event1' : [], 'event2': [] }

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer)

    @classmethod
    def unregister(cls, observer):
        if observer in cls._observers:
            cls._observers.remove(observer)

    @classmethod
    def notify(cls, event, data=None):
        for observer in cls._observers:
            observer(event, data)


def logger(event, data):
    print(event, data)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'a') as fl:
            fl.write(f"{datetime.datetime.now()}: [{event}] - {data}\n")


if __name__ == '__main__':
    Event.register(logger)
    fl = FileLogger('logs.txt')
    Event.register(fl)

    Event.notify('PULS', 65)
    Event.notify('PULS', 67)
    Event.notify('PULS', 69)
    Event.notify('UPS', 'Sometime it happens')
    Event.unregister(fl)
    Event.notify('PULS', 120)
    Event.notify('PULS', 130)