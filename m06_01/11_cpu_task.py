import asyncio
from concurrent.futures import ProcessPoolExecutor
import datetime


def cpu_bound_task(counter):
    init = counter
    while counter > 0:
        counter -= 1
    print(f"Completed task for {init}")
    return init


async def worker():
    loop = asyncio.get_running_loop()
    loop.create_task(tiker())
    with ProcessPoolExecutor(5) as executor:
        futures = [loop.run_in_executor(executor, cpu_bound_task, num) for num in [50_000_000, 60_000_000, 70_000_000]]
        r = await asyncio.gather(*futures)
        return r


async def tiker():
    while True:
        await asyncio.sleep(1)
        print(datetime.datetime.now())


if __name__ == '__main__':
    r = asyncio.run(worker())
    print(r)
