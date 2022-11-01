import asyncio
from concurrent.futures import ThreadPoolExecutor
from time import time

import requests

urls = ["https://nodejs.org/uk/", "https://www.python.org/", "https://faker.readthedocs.io/", "https://github.com/",
        "https://goit.global/ua/"]


def get_url_info(url):
    r = requests.get(url)
    return url, r.text[:50]


async def get_url_info_async(urls):
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor(5) as executor:
        futures = [loop.run_in_executor(executor, get_url_info, url) for url in urls]
        r = await asyncio.gather(*futures)
        return r

if __name__ == '__main__':
    start = time()
    results = [get_url_info(url) for url in urls]
    print(results)
    print(time() - start)
    print("------------")
    start = time()
    results = asyncio.run(get_url_info_async(urls))
    print(results)
    print(time() - start)