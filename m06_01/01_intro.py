import asyncio


async def baz():
    print('Run function baz')
    await asyncio.sleep(1)
    return 'Hello world!'


async def main():
    r = baz()
    print(r)
    result = await r
    print(result)
    return 'End'


if __name__ == '__main__':
    r = asyncio.run(main())
    print(r)
