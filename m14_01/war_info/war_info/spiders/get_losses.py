import json
import re
from datetime import datetime

import scrapy


class GetLossesSpider(scrapy.Spider):
    name = 'get_losses'
    allowed_domains = ['index.minfin.com.ua']
    start_urls = ['https://index.minfin.com.ua/ua/russian-invading/casualties/']

    @staticmethod
    def get_next_link():
        with open('links.json') as fd:
            r = json.load(fd)
        return [el.get('link') for el in r]

    def parse(self, response):
        result = {}
        for element in response.css("ul[class=see-also] li[class=gold]"):
            date = element.xpath("span/text()").get()
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError:
                print(f'Error for {date}')
                continue

            result.update({'date': date})
            losses = element.xpath("div/div/ul/li")
            for lose in losses:
                # print(' '.join(lose.css("::text").extract()).split('—'))
                title, quantity = ' '.join(lose.css("::text").extract()).split('—')
                title = title.strip()
                quantity = re.search(r"\d+", quantity).group()
                result.update({title: quantity})
            yield result

        for next_link in self.get_next_link():
            yield scrapy.Request(url=self.start_urls[0] + next_link)