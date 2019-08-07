# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZlzpItem(scrapy.Item):
    job_name=scrapy.Field()
    salary = scrapy.Field()
    address = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    want_numbers = scrapy.Field()
    update_time = scrapy.Field()
    workplace = scrapy.Field()
    url= scrapy.Field()
