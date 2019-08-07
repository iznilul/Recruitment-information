# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengwuyouItem(scrapy.Item):
	job_name = scrapy.Field()
	salary = scrapy.Field()
	company = scrapy.Field()
	degree = scrapy.Field()
	demand = scrapy.Field()
	experience = scrapy.Field()
	want_numbers = scrapy.Field()
	dateline = scrapy.Field()
	category = scrapy.Field()
	keyword = scrapy.Field()
	address = scrapy.Field()
	url = scrapy.Field()


