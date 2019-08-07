# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from baixing.settings import *
import pymysql
import logging
class AbroadwebsitePipeline(object):
    def __init__(self):
        self.connect=pymysql.connect(MYSQL_HOST,MYSQL_ROOT,MYSQL_PASSWORD,MYSQL_DATABASE)
        self.cursor=self.connect.cursor()
        self.cursor.execute(USE)  # 选定数据库
        self.cursor.execute(DROP)
        self.cursor.execute(CREATE)

    def process_item(self, item, spider):
        try:
            self.cursor.execute(SAVEIN,(item['title'],item["update_time"],item["salary"],item["company"],item["address"],
                            item["category"],item["want_numbers"],item["degree"],item["experience"],item["tag"],item["gender_demand"],item["url"]))
            self.connect.commit()
        except Exception as error:
            logging.log(error)
        return item,
    def close_spider(self,spider):
        self.connect.close()

class BaixingPipeline(object):
    def process_item(self, item, spider):
        return item
