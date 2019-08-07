# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RencaiItem(scrapy.Item):
    job_name=scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    degree = scrapy.Field()
    experience = scrapy.Field()
    want_numbers = scrapy.Field()
    category = scrapy.Field()
    tag = scrapy.Field()
    workplace = scrapy.Field()
    update_time = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
