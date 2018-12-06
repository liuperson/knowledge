# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql


# class Maoyan2Pipeline(object):
#     def __init__(self,host,port,database,user,password):
#         self.host=host
#         self.port=port
#         self.database=database
#         self.user=user
#         self.password=password
#
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             host=crawler.settings.get('MYSQL_HOST'),
#             port=crawler.settings.get('MYSQL_PORT'),
#             database=crawler.settings.get('MYSQL_DATABASE'),
#             user=crawler.settings.get('MYSQL_USER'),
#             password=crawler.settings.get('MYSQL_PASSWORD')
#
#         )
#     def open_spider(self,spider):
#         self.db=pymysql.connect(self.host,self.user,self.password,self.database,charset='utf8',port=self.port)
#         self.cursor=self.db.cursor()
#
#     def close_spider(self,spider):
#         self.db.close()
#
#
#     def process_item(self, item, spider):
#         sql="insert into movie (name,actor,release_time,score) values ('%s','%s','%s','%s')"% (item['name'],item['actor'],item['release_time'],item['score'])
#         self.cursor.execute(sql)
#         self.db.commit()
#         return item





# import pymongo
#
# class Maoyan2MongoDBPipeline(object):
#     def __init__(self,mongo_db):
#         self.mongodb=mongo_db
#
#
#     def open_spider(self,spider):
#         self.client=pymongo.MongoClient()
#         self.db = self.client[self.mongodb]
#
#     def close_spider(self,spider):
#         self.db.close()
#
#     def process_item(self, item, spider):
#         movie={}
#         movie['name']=item['name']
#         movie['actor']=item['actor']
#         movie['release_time']=item['release_time']
#         movie['score']=item['score']
#         self.db.movies.insert(movie)
#         return item
#
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             mongo_db=crawler.settings.get('MONGO_DB')
#         )





# from mongoengine import *
#
# class Movie(Document):
#     name=StringField(max_length=512)
#     actor=StringField(max_length=512)
#     release_time=StringField(max_length=128)
#     score=StringField(max_length=128)
#
# class Maoyan2MongoenginePipeline(object):
#     def __init__(self,database):
#         self.db=database
#
#     def open_spider(self,spider):
#         connect(self.db)
#
#     def close_spider(self,spider):
#         pass
#
#     def process_item(self, item, spider):
#         movie=Movie()
#         movie['name']=item['name']
#         movie['actor']=item['actor']
#         movie['release_time']=item['release_time']
#         movie['score']=item['score']
#         movie.save()
#         return item
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         return cls(
#             database=crawler.settings.get('MONGO_DB')
#         )
