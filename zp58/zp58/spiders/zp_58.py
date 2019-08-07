# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zp58.items import *

class Zp58Spider(CrawlSpider):
    name = 'zp_58'
    # allowed_domains = ['www.58.com']
    start_urls = ['https://as.58.com/job/?PGTID=0d100000-0020-b1e9-60c2-6c3c00bd1a68&ClickID=2#&key=']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//*[@class="job_name clearfix"]/a'), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="next"]'))
    )

    def parse_item(self, response):
        item=Zp58Item()
        item["job_name1"]=response.xpath('//*[@class="pos_title"]/text()').extract_first()
        item["job_name2"] = response.xpath('//*[@class="pos_name"]/text()').extract_first()
        # try:
        #     response.xpath('//*[@class="pos_salary"]/text()')
        #     a = True
        # except:
        #     response.xpath('//*[@class="pos_salary daiding"]/text()')
        #     a = False
        # if a == True:
        #     item["salary"] = response.xpath('//*[@class="pos_salary"]/text()').extract_first()
        # elif a == False:
        #     item["salary"] = response.xpath('//*[@class="pos_salary daiding"]/text()').extract_first()
        item["salary"] = response.xpath('//*[@class="pos_salary"]/text()').extract_first()
        item["want_numbers"] = response.xpath('//*[@class="item_condition pad_left_none"]/text()').extract_first()
        item["degree"] = response.xpath('//*[@class="item_condition"]/text()').extract_first()
        item["experience"] = response.xpath('//*[@class="item_condition border_right_None"]/text()').extract_first()
        if len(response.xpath('//*[@class="pos_area_item"]/text()').extract())>1:
            item["address1"] = response.xpath('//*[@class="pos_area_item"]/text()').extract()[0]+" "+response.xpath('//*[@class="pos_area_item"]/text()').extract()[1]
        else:
            item["address1"] = response.xpath('//*[@class="pos_area_item"]/text()').extract_first()
        item["address2"] = response.xpath('//*[@class="pos-area"]/span[2]/text()').extract_first()
        item["url"] = response.url
        yield item

