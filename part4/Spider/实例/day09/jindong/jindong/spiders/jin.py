# -*- coding: utf-8 -*-
import scrapy


class JinSpider(scrapy.Spider):
    name = 'jin'
    allowed_domains = ['www.jd.com']
    start_urls = ['http://www.jd.com/']

    def start_requests(self):
        for keyword in self.settings.get('KEYWORD'):
            pass






    def parse(self, response):
        pass




