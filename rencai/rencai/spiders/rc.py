# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from rencai.items import *

class RcSpider(CrawlSpider):
    name = 'rc'
    # allowed_domains = ['www.shit.com']
    start_urls = ['http://s.cjol.com/?SearchType=3&RecruitmentType=1&defaultmust=0&',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=2&defaultmust=0',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=3&defaultmust=0']

    rules = (
        Rule(LinkExtractor(allow='',restrict_xpaths=('//*[@class="list_type_first"]/h3/a')), callback='parse_item'),
        # Rule(LinkExtractor(restrict_xpaths=('//*[@class="pagination"]/a[last()]')))
    )


    def parse_item(self, response):
        item=RencaiItem()
        item["job_name"]=response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/text()').extract_first()
        item["company"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/a/text()').extract_first()
        item["salary"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[1]/em/text()').extract_first()
        item["degree"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[2]/text()').extract_first()
        item["experience"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[3]/text()').extract_first()
        item["want_numbers"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[4]/text()').extract_first()
        item["category"] = response.xpath('/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[5]/text()').extract_first()
        tags = response.xpath('//*[@class="taglist-jobintro clearfix"]/li/text()').extract()
        list = []
        for i in tags:
            list.append(i)
        i_s1 = " ".join(list)
        item["tag"]=i_s1
        item["workplace"] = response.xpath('//*[@class="area-jobintro f_l"]/@title').extract_first()
        item["update_time"] = response.xpath('//*[@class="pubtime-jobintro f_l"]/text()').extract_first()
        item["address"] = response.xpath('//*[@class="txtinfo-address"]/text()').extract_first()
        item["url"] = response.url
        yield item
