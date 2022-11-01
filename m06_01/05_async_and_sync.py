import asyncio
from faker import Faker
from time import sleep, time
from typing import Awaitable, Iterable, List

fake = Faker()


async def get_user_async(uid: int):
    await asyncio.sleep(0.5)
    return {"id": uid, "name": fake.name(), "company": fake.company(), "email": fake.email()}


def get_users(uids: List[int]) -> Iterable[Awaitable]:
    return [get_user_async(uid) for uid in uids]


async def main(users: Iterable[Awaitable]):
    return await asyncio.gather(*users)  # await asyncio.gather(get_user_async(1), get_user_async(2), get_user_async(3))


if __name__ == '__main__':
    start = time()
    users = asyncio.run(main(get_users([1, 2, 3])))
    print(users)
    print(time() - start)
