# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdmissionszpItem(scrapy.Item):
    title=scrapy.Field()
    datetime=scrapy.Field()
    workplace=scrapy.Field()
    category=scrapy.Field()
    where_from=scrapy.Field()
    position=scrapy.Field()
    tag=scrapy.Field()
    others=scrapy.Field()
    demand=scrapy.Field()
    url=scrapy.Field()
