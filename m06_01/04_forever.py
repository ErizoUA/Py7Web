import asyncio
from time import time


async def send_metrics(url: str):
    print(f'Send to {url}: {time()}')


async def worker():
    while True:
        await asyncio.sleep(1)
        await send_metrics('https://logstage.com.ua')


async def worker_two():
    while True:
        await asyncio.sleep(2)
        await send_metrics('https://babadum.com')


async def main(loop: asyncio.new_event_loop):
    loop.create_task(worker())
    loop.create_task(worker_two())


async def main_run():
    asyncio.create_task(worker())
    await asyncio.create_task(worker_two())


if __name__ == '__main__':
    asyncio.run(main_run())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.create_task(main(loop))
    # loop.run_forever()
