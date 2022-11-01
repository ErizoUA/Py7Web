import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def io_ops():
    with open('main.py') as f:
        return f.read(50)


def cpu_ops(power: int, count: int):
    r = [i ** power for i in range(10 * count)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    r = await loop.run_in_executor(None, io_ops)
    print(r)

    r = await loop.run_in_executor(None, cpu_ops, 2, 5)
    print(r)

    with ThreadPoolExecutor() as executor:
        r = await loop.run_in_executor(executor, io_ops)
        print(r)

    with ProcessPoolExecutor() as executor:
        r = await loop.run_in_executor(executor, cpu_ops, 2, 5)
        print(r)

if __name__ == '__main__':
    asyncio.run(main())
