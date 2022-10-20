from datetime import datetime, timedelta
from typing import List
import concurrent.futures
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
    # r.append("error date")
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


def worker(date: str) -> dict:
    try:
        r = get_rates(date)
    except Exception as err:
        return {date: err}
    else:
        return {date: r}


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE) as executor:
        # futures = []
        # for date in get_dates(3):
        #     futures.append(executor.submit(worker, date))
        # for f in concurrent.futures.as_completed(futures):
        #     print(f.result())
        for r in executor.map(worker, get_dates(3)):
            print(r)


if __name__ == '__main__':
    main()


