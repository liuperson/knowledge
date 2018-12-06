# -*- coding: utf-8 -*-
import scrapy
import json

from zhancool.agent_helper import get_random_agent


class ZhancoolItem(scrapy.Item):
    title=scrapy.Field()
    item_id=scrapy.Field()
    preview_url=scrapy.Field()





class CoolSpider(scrapy.Spider):
    name = 'cool'
    allowed_domains = ['api.hellorf.com']
    start_urls = ['http://www.hellorf.com/']

    def start_requests(self):

        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Host': 'api.hellorf.com'
        }

        for i in range(1,3):
            data={'keyword':'网站','page':str(i)}
            headers['User-Agent'] = get_random_agent()
            yield scrapy.FormRequest(url='https://api.hellorf.com/hellorf/image/search?page=%d'%i ,
                             headers=headers,
                             formdata=data,
                             method='POST',
                             callback=self.parse,
                             )



    def parse(self, response):
        re=json.loads(response.text)
        data_list=re['data']['data']
        for data in data_list:
            item=ZhancoolItem()
            item['item_id']=data.get('_id','')
            item['title']=data.get('title','')
            item['preview_url']=data.get('preview_url','')
            yield item

