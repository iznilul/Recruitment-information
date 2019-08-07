# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Zp58Item(scrapy.Item):
    job_name1=scrapy.Field()
    job_name2 = scrapy.Field()
    salary = scrapy.Field()
    want_numbers = scrapy.Field()
    degree = scrapy.Field()
    experience = scrapy.Field()
    address1 = scrapy.Field()
    address2 = scrapy.Field()
    url = scrapy.Field()


