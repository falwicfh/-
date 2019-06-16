# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
#from music163list.settings import mongo_db_collection,mongo_db_name,mongo_port,mongo_host
from scrapy.conf import settings
#db class
class Music163ListPipeline(object):

    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[settings['MONGODB_DOCNAME']]

    def process_item(self, item, spider):
        person_info = dict(item)
        self.post.insert(person_info)
        return item

    #def __init__(self):
    #    self.snapshot_coll = pymongo.MongoClient(host=settings['MONGO_HOST'])[settings['MONGO_DB']][settings['SNAPSHOT_COLL']]
    #    self.film_coll = pymongo.MongoClient(host=settings['MONGO_HOST'])[settings['MONGO_DB']][settings['FILM_COLL']]