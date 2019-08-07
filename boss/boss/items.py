# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    job_name=scrapy.Field()
    salary = scrapy.Field()
    place = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    tag = scrapy.Field()
    information = scrapy.Field()
    address = scrapy.Field()
    url = scrapy.Field()
