from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://userweb7:567234@krabaton.5mlpr.gcp.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))
db = client.web7

if __name__ == '__main__':
    result_many = db.cats.insert_many(
        [
            {
                "name": "Lama",
                "age": 2,
                "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
            },
            {
                "name": "Liza",
                "age": 4,
                "features": ["ходить в лоток", "дає себе гладити", "білий"],
            },
            {
                "name": "Yuriy",
                "age": 38,
                "status": "maried",
                "gender": "male",
                "features": ["ходить на лекції", "задає запитання", "білий"],
            },
        ]
    )
    print(result_many)
    result = db.cats.find()
    for r in result:
        print(r)
