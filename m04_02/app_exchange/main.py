from datetime import datetime, timedelta
from typing import List
from queue import Queue, Empty
from threading import Thread
import requests

BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates"
THREAD_POOL_SIZE = 2


def get_dates(total_days=7) -> List[str]:
    r = []
    today = datetime.now()
    for d in range(total_days):
        date_shift = today - timedelta(days=d)
        string_date = datetime.strftime(date_shift, "%d.%m.%Y")
        r.append(string_date)
    r.append("error date")
    return r


def get_rates(date: str) -> dict:
    url = f"{BASE_URL}?json&date={date}"
    response = requests.get(url)
    exchange_rate = response.json()["exchangeRate"]
    rates = list(filter(lambda el: el.get("currency", None) in ["EUR", "USD"], exchange_rate))
    rates = list(map(lambda el: {
        el.get("currency", None): {"sale": el.get("saleRate", None), "purchase": el.get("purchaseRate", None)}}, rates))
    r = {}
    for el in rates:
        r.update(el)
    return r


def worker(source_date: Queue, results: Queue):
    while not source_date.empty():
        try:
            date = source_date.get()
        except Empty:
            break
        else:
            try:
                r = get_rates(date)
            except Exception as err:
                results.put({date: err})
            else:
                results.put({date: r})
            finally:
                source_date.task_done()


if __name__ == '__main__':
    source_date = Queue()
    results = Queue()

    for date in get_dates(3):
        source_date.put(date)

    threads = [Thread(target=worker, args=(source_date, results)) for _ in range(THREAD_POOL_SIZE)]
    [th.start() for th in threads]
    source_date.join()
    [th.join() for th in threads]

    while not results.empty():
        result = results.get()
        print(result)


