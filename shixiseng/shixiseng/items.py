# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShixisengItem(scrapy.Item):
    job_name=scrapy.Field()
    update_time = scrapy.Field()
    salary = scrapy.Field()
    place = scrapy.Field()
    degree = scrapy.Field()
    weekly_time = scrapy.Field()
    total_time = scrapy.Field()
    tag= scrapy.Field()
    company = scrapy.Field()
    workplace = scrapy.Field()
    deadline = scrapy.Field()
    url=scrapy.Field()