import asyncio
import aiohttp
import platform
from aiohttp.client_exceptions import ClientConnectorError

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


async def main():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(URL) as response:
                if response.status == 200:
                    result = await response.json()
                    print(result)
                else:
                    print(f"Error status: {response.status} for {URL}")
        except ClientConnectorError as e:
            print(f"Connection error for {URL}: {e}")


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
