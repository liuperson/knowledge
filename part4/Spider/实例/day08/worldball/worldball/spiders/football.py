# -*- coding: utf-8 -*-


import scrapy


class WorldballItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()



class FootballSpider(scrapy.Spider):
    name = 'football'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/g/2018worldcupeq//']

    def parse(self, response):
        headlines = response.selector.css('.-live-page-widget a::text').extract()
        print('-' * 20)
        print(headlines)
        for title in headlines:
            item = WorldballItem()
            item['title'] = title
            yield item

