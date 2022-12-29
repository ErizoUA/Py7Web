import json

import scrapy
from scrapy.crawler import CrawlerProcess
from itemadapter import ItemAdapter


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    bio = scrapy.Field()


class SpiderPipeline(object):
    quotes = []
    authors = []

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if 'author' in adapter.keys():
            self.quotes.append({
                "tags": adapter['tags'],
                "author": adapter['author'],
                "quote": adapter['quote'],
            })
        if 'fullname' in adapter.keys():
            self.authors.append({
                "fullname": adapter['fullname'],
                "born_date": adapter['born_date'],
                "born_location": adapter['born_location'],
                "bio": adapter['bio'],
            })
        return item

    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as fd:
            json.dump(self.quotes, fd, ensure_ascii=False)

        with open('authors.json', 'w', encoding='utf-8') as fd:
            json.dump(self.authors, fd, ensure_ascii=False)


class Spider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'ITEM_PIPELINES': {
            SpiderPipeline: 300,
        }
    }

    def parse(self, response):
        for quote in response.xpath("/html//div[@class='quote']"):
            yield response.follow(url=self.start_urls[0] + quote.xpath('span/a/@href').get(),
                                  callback=self.parse_author)

        for quote in response.xpath("/html//div[@class='quote']"):
            tags = quote.xpath("div[@class='tags']/a/text()").extract()
            author, = quote.xpath("span/small/text()").get(),
            quote = quote.xpath("span[@class='text']/text()").get()
            yield QuoteItem(author=author, quote=quote, tags=tags)

        next_link = response.xpath("//li[@class='next']/a/@href").get()
        if next_link:
            yield scrapy.Request(url=self.start_urls[0] + next_link)

    def parse_author(self, response):
        content = response.xpath("/html//div[@class='author-details']")
        fullname = content.xpath("h3/text()").get().strip()
        born_date = content.xpath("p/span[@class='author-born-date']/text()").get().strip()
        born_location = content.xpath("p/span[@class='author-born-location']/text()").get().strip()
        bio = content.xpath("div[@class='author-description']/text()").get().strip()
        yield AuthorItem(fullname=fullname, born_date=born_date, bio=bio, born_location=born_location)


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(Spider)
    process.start()
