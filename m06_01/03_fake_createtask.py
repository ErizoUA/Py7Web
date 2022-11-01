import asyncio
from faker import Faker
from time import sleep, time

fake = Faker()


async def get_user_async(uid: int):
    await asyncio.sleep(0.5)
    return {"id": uid, "name": fake.name(), "company": fake.company(), "email": fake.email()}


async def main():
    u1 = asyncio.create_task(get_user_async(1))
    u2 = asyncio.create_task(get_user_async(2))
    u3 = asyncio.create_task(get_user_async(3))

    # result = await asyncio.gather(u1, u2, u3)
    # return result
    return [await u1, await u2, await u3]


if __name__ == '__main__':
    start = time()
    # users = asyncio.run(main())
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    users = loop.run_until_complete(main())
    print(users)
    print(time() - start)
    loop.close()
