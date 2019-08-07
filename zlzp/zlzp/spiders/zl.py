# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zlzp.items import *
from scrapy import Request
class ZlSpider(CrawlSpider):
    name = 'zl'
    # allowed_domains = ['www.zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/?jl=530&kw=Java%E5%BC%80%E5%8F%91&kt=3',
'https://sou.zhaopin.com/?jl=530&kw=UI%E8%AE%BE%E8%AE%A1%E5%B8%88&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=Web%E5%89%8D%E7%AB%AF&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=PHP&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=Python&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=Android&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E7%BE%8E%E5%B7%A5&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=Hadoop&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=Node.js&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%BC%80%E5%8F%91&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%B8%88&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E6%95%B0%E6%8D%AE%E6%9E%B6%E6%9E%84&kt=3&sf=0&st=0',
'https://sou.zhaopin.com/?jl=530&kw=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&kt=3&sf=0&st=0',
]


    rules = (
        Rule(LinkExtractor(allow='jobs.zhaopin.com',restrict_xpaths='//*[@class="contentpile__content__wrapper__item clearfix"]/a'),callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths='//*[@class="btn soupager__btn"]'))
    )

    def parse_item(self, response):
        item=ZlzpItem()
        item["job_name"]=response.xpath('//*[@id="root"]/div[3]/div/div/h3/text()').extract_first()
        item["salary"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/span/text()').extract_first()
        item["want_numbers"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[4]/text()').extract_first()
        item["degree"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[3]/text()').extract_first()
        item["experience"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[2]/text()').extract_first()
        item["update_time"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[1]/span/text()').extract_first()
        if response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[1]/span/text()')is not None:
            item["address"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a/text()').extract_first()+" "+response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[1]/span/text()').extract_first()
        else:
            item["address"] = response.xpath('//*[@id="root"]/div[3]/div/div/div[2]/div[1]/ul/li[1]/a/text()').extract_first()
        item["workplace"] = response.xpath('//*[@id="root"]/div[4]/div[1]/div[1]/div[3]/div/span/text()').extract_first()
        item["url"] = response.url
        yield item
