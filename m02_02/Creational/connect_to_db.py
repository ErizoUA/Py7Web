from dataclasses import dataclass


class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


# class Settings(metaclass=MetaSingleton):
#     def __init__(self):
#         self.db = 'MySQL'
#         self.port = 3306

@dataclass
class Settings(metaclass=MetaSingleton):
     db: str = 'MySQL'
     port: int = 3306


connect = Settings()

connect_other = Settings()

print(connect_other.port)
connect.port = 5634
print(connect_other.port)
