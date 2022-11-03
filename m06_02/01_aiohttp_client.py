import asyncio
import aiohttp
import platform
from aiohttp.client_exceptions import ClientConnectorError

urls = ['http://www.google.com', 'http://www.python.org', 'http://duckduckgo.com', 'http://www.python.org/asdf',
        'http://test']


async def main():
    async with aiohttp.ClientSession() as session:
        for url in urls:
            try:
                async with session.get(url) as response:
                    if response.status == 200:
                        text = await response.text()
                        print(url, text[:150])
                    else:
                        print(f"Error status: {response.status} for {url}")
            except ClientConnectorError as e:
                print(f"Connection error for {url}: {e}")


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
