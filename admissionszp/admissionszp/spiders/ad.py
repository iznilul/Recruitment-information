# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from admissionszp.items import *

class AdSpider(CrawlSpider):
    name = 'ad'
    # allowed_domains = ['www.jfie.com']
    start_urls = ['http://www.yingjiesheng.com/beijing-morejob-1.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//*[@class="item1"]/a')), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=('//*[@class="page"]/a[@title="next page"]')))
    )

    def parse_item(self, response):
        item=AdmissionszpItem()
        if response.xpath('//*[@class="main mleft"]/h1/text()').extract_first() is not None:
            item["title"] = response.xpath('//*[@class="main mleft"]/h1/text()').extract_first()
        else:
            item["title"] = response.xpath('//*[@class="mleft"]/h1/text()').extract_first()
        item["datetime"] = response.xpath('//*[@class="info clearfix"]/ol/li[1]/u/text()').extract_first()
        item["workplace"] = response.xpath('//*[@class="info clearfix"]/ol/li[2]/u/text()').extract_first()
        item["category"] = response.xpath('//*[@class="info clearfix"]/ol/li[3]/u/text()').extract_first()
        item["where_from"] = response.xpath('//*[@class="info clearfix"]/ol/li[4]/a/text()').extract_first()
        item["position"] = response.xpath('//*[@class="info clearfix"]/ol/li[5]/u/text()').extract_first()
        tags=response.xpath('//*[@id="container"]/div[1]/div[2]/a/text()').extract()
        list=[]
        for i in tags:
            list.append(str(i))
        i_s1=" ".join(list)
        item["tag"]=i_s1
        item["others"] = response.xpath('//*[@id="wordDiv"]/div/div[1]/text()').extract_first()
        demands= response.xpath('//*[@id="wordDiv"]/div/div[1]/p/text()').extract()
        list = []
        for i in demands:
            list.append(str(i))
        i_s2 = " ".join(list)
        item["demand"] = i_s2
        item["url"]=response.url
        yield item