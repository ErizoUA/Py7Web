import asyncio
import aiohttp
import platform
from aiohttp.client_exceptions import ClientConnectorError

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com', 'http://www.python.org/asdf',
        'https://test']


async def main():
    session = aiohttp.ClientSession()
    for url in urls:
        try:
            response = await session.get(url)
            if response.status == 200:
                text = await response.text()
                print(url, text[:150])
            else:
                print(f"Error status: {response.status} for {url}")
        except ClientConnectorError as e:
            print(f"Connection error for {url}: {e}")
    await session.close()


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
