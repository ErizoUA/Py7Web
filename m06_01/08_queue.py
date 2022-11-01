import asyncio
import random
import queue


async def producer(q: asyncio.Queue):
    num = random.randint(1, 100)
    await asyncio.sleep(0.25)
    await q.put(num)


async def consumer(q: asyncio.Queue, result: queue.Queue):
    while True:
        num = await q.get()
        r = num ** 2
        result.put((num, r))
        q.task_done()


async def main():
    q = asyncio.Queue()
    r = queue.Queue()
    consumers = [asyncio.create_task(consumer(q, r)) for _ in range(5)]
    producers = [asyncio.create_task(producer(q)) for _ in range(10)]
    await asyncio.gather(*producers)
    await q.join()
    [con.cancel() for con in consumers]
    return r

if __name__ == '__main__':
    res = asyncio.run(main())
    while not res.empty():
        print(res.get())

