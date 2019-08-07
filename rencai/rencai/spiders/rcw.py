# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from rencai.items import *
from urllib.parse import urlencode
class RcwSpider(scrapy.Spider):
    name = 'rcw'
    s_1=999
    s_2=55
    s_3=35
    # allowed_domains = ['www.shit.com']
    start_urls = ['http://s.cjol.com/?SearchType=3&RecruitmentType=1&defaultmust=0&',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=2&defaultmust=0&',
                  'http://s.cjol.com/?SearchType=3&RecruitmentType=3&defaultmust=0&']
    def start_requests(self):
        for i in range(len(self.start_urls)):
           now_url=self.start_urls[i]
           if i==0:
               for s in range(self.s_1):
                   data = {
                       "page": s+1
                   }
                   params = urlencode(data)
                   new_url=now_url+params
                   yield Request(new_url,callback=self.get)
           if i==1:
               for s in range(self.s_2):
                   data = {
                       "page": s+1
                   }
                   params = urlencode(data)
                   new_url=now_url+params
                   yield Request(new_url,callback=self.get)
           if i == 2:
               for s in range(self.s_3):
                   data = {
                       "page": s + 1
                   }
                   params = urlencode(data)
                   new_url = now_url + params
                   yield Request(new_url, callback=self.get)
    def get(self, response):
        job_urls=response.xpath('//*[@class="list_type_first"]/h3/a/@href').extract()
        for job_url in job_urls:
            yield Request(job_url,callback=self.parse)
    def parse(self,response):
        item = RencaiItem()
        item["job_name"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/text()').extract_first()
        item["company"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[1]/div[1]/div[2]/a/text()').extract_first()
        item["salary"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[1]/em/text()').extract_first()
        item["degree"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[2]/text()').extract_first()
        item["experience"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[3]/text()').extract_first()
        item["want_numbers"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[4]/text()').extract_first()
        item["category"] = response.xpath(
            '/html/body/div[4]/div[1]/div/div[1]/div/div[2]/ul[1]/li[5]/text()').extract_first()
        tags = response.xpath('//*[@class="taglist-jobintro clearfix"]/li/text()').extract()
        list = []
        for i in tags:
            list.append(i)
        i_s1 = " ".join(list)
        item["tag"] = i_s1
        item["workplace"] = response.xpath('//*[@class="area-jobintro f_l"]/@title').extract_first()
        item["update_time"] = response.xpath('//*[@class="pubtime-jobintro f_l"]/text()').extract_first()
        item["address"] = response.xpath('//*[@class="txtinfo-address"]/text()').extract_first()
        item["url"] = response.url
        yield item