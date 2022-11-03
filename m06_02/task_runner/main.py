import asyncio
from aiofile import async_open
from aiopath import AsyncPath
import logging


async def consumer(filename: str, queue: asyncio.Queue):
    async with async_open(filename, "w", encoding="utf-8") as afp:
        while True:
            file, data = await queue.get()
            logging.info(f"operation write with file {file.name}")
            await afp.write(f"{data}\n")
            queue.task_done()


async def producer(file: AsyncPath, queue: asyncio.Queue):
    async with async_open(file, "r", encoding="utf-8") as afp:
        data = await afp.read()
        await queue.put((file, data))
        logging.info(f"operation read completed with file {file.name}")


async def main():
    result_queue = asyncio.Queue()
    list_files = AsyncPath('.').joinpath("files").glob('*.js')
    logging.info(list_files)
    producers = [producer(file, result_queue) async for file in list_files]
    c = asyncio.create_task(consumer('main.js', result_queue))
    await asyncio.gather(*producers)
    await result_queue.join()
    c.cancel()
    logging.info('Completed')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    asyncio.run(main())
