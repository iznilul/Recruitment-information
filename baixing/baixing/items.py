# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaixingItem(scrapy.Item):
	title=scrapy.Field()
	update_time=scrapy.Field()
	salary = scrapy.Field()
	company = scrapy.Field()
	address = scrapy.Field()
	category = scrapy.Field()
	want_numbers = scrapy.Field()
	degree = scrapy.Field()
	experience = scrapy.Field()
	tag = scrapy.Field()
	gender_demand = scrapy.Field()
	url = scrapy.Field()

