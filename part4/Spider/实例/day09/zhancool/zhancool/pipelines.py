# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline



class ZhancoolimagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 构造图片url请求
        # 返回图片文件名
        yield Request(item['preview_url'])

    def file_path(self, request, response=None, info=None):
        url=request.url
        filename=url.split('/')[-1]
        return filename

    def item_completed(self, results, item, info):
        # 判断图片下载的请求是否成功
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item


