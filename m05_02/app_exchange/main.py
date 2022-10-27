from datetime import datetime, timedelta
from typing import List
from multiprocessing import Pool, cpu_count
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


def worker(date_: str):
    try:
        r = get_rates(date_)
    except Exception as err:
        return {date_: err}
    else:
        return {date_: r}


if __name__ == '__main__':
    dates = get_dates()
    with Pool(cpu_count()) as pool:
        pool.map_async(worker, dates, callback=print)
        pool.close()
        pool.join()

