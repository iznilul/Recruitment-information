# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiItem(scrapy.Item):
	job1=scrapy.Field()
	job2=scrapy.Field()
	salary=scrapy.Field()
	want_numbers=scrapy.Field()
	degree=scrapy.Field()
	admissions= scrapy.Field()
	experience= scrapy.Field()
	age= scrapy.Field()
	address= scrapy.Field()
	url=scrapy.Field()



