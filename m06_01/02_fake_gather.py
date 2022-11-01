import asyncio
from faker import Faker
from time import sleep, time

fake = Faker()


def get_user_sync(uid: int):
    sleep(0.5)
    return {"id": uid, "name": fake.name(), "company": fake.company(), "email": fake.email()}


async def get_user_async(uid: int):
    await asyncio.sleep(0.5)
    return {"id": uid, "name": fake.name(), "company": fake.company(), "email": fake.email()}


async def main():
    users = [get_user_async(uid) for uid in [1, 3, 4]]
    result = await asyncio.gather(*users)
    return result


if __name__ == '__main__':
    start = time()
    users = []
    for uid in [1, 3, 4]:
        users.append(get_user_sync(uid))
    print(users)
    print(time() - start)
    print("------------------------")
    start = time()
    users = asyncio.run(main())
    print(users)
    print(time() - start)
