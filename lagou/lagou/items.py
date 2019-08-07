# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    job_name=scrapy.Field()
    salary = scrapy.Field()
    place = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    category = scrapy.Field()
    update_time = scrapy.Field()
    tag = scrapy.Field()
    workplace = scrapy.Field()
    address = scrapy.Field()
    company=scrapy.Field()
    url=scrapy.Field()
