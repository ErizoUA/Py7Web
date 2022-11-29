import argparse
from functools import wraps

from bson import ObjectId
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client.web7

parser = argparse.ArgumentParser(description='Cats APP')
parser.add_argument('--action', help='Command: create, update, find, remove')
parser.add_argument('--id')
parser.add_argument('--name')
parser.add_argument('--age')
parser.add_argument('--features', nargs='+')

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
name = my_arg.get('name')
age = my_arg.get('age')
_id = my_arg.get('id')
features = my_arg.get('features')


class ExceptValidation(Exception):
    pass


def validate(func):
    @wraps(func)
    def wrapper(*args):
        for el in args:
            if el is None:
                raise ExceptValidation(f"Вхідні дані не валідні {func.__name__}{args}")
        result = func(*args)
        return result
    return wrapper


def find_by_id(_id):
    result = db.cats.find_one({"_id": ObjectId(_id)})
    return result


def find():
    return db.cats.find()


@validate
def create(name, age, features):
    result_one = db.cats.insert_one(
        {
            "name": name,
            "age": age,
            "features": features,
        }
    )
    return find_by_id(result_one.inserted_id)


@validate
def update(_id, name, age, features):
    db.cats.update_one({"_id": ObjectId(_id)}, {"$set": {
            "name": name,
            "age": age,
            "features": features,
        }})
    return find_by_id(_id)


@validate
def remove(_id):
    db.cats.delete_one({"_id": ObjectId(_id)})
    return find_by_id(_id)


def main():
    try:
        match action:
            case 'create':
                r = create(name, age, features)
                print(r)
            case 'find':
                r = find()
                [print(el) for el in r]
            case 'update':
                r = update(_id, name, age, features)
                print(r)
            case 'remove':
                r = remove(_id)
                print(r)
            case _:
                print("Unknowns command")

    except ExceptValidation as err:
        print(err)


if __name__ == '__main__':
    main()

