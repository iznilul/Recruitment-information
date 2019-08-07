# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from shixiseng.items import *

class SxsSpider(CrawlSpider):
    name = 'sxs'
    # allowed_domains = ['www.shit.com']
    start_urls = ['https://www.shixiseng.com/interns/?keyword=Java&',
'https://www.shixiseng.com/interns/?keyword=UI设计师&',
'https://www.shixiseng.com/interns/?keyword=Web前端&',
'https://www.shixiseng.com/interns/?keyword=PHP&',
'https://www.shixiseng.com/interns/?keyword=Python&',
'https://www.shixiseng.com/interns/?keyword=Android&',
'https://www.shixiseng.com/interns/?keyword=美工&',
'https://www.shixiseng.com/interns/?keyword=深度学习&',
'https://www.shixiseng.com/interns/?keyword=算法工程师&',
'https://www.shixiseng.com/interns/?keyword=Hadoop&',
'https://www.shixiseng.com/interns/?keyword=Node.js&',
'https://www.shixiseng.com/interns/?keyword=数据开发&',
'https://www.shixiseng.com/interns/?keyword=数据分析师&',
'https://www.shixiseng.com/interns/?keyword=数据架构&',
'https://www.shixiseng.com/interns/?keyword=人工智能&',
'https://www.shixiseng.com/interns/?keyword=区块链&',
'https://www.shixiseng.com/interns/?keyword=电气工程&',
'https://www.shixiseng.com/interns/?keyword=销售&',
'https://www.shixiseng.com/interns/?keyword=金融&',
'https://www.shixiseng.com/interns/?keyword=英语&',
'https://www.shixiseng.com/interns/?keyword=数据挖掘&',
'https://www.shixiseng.com/interns/?keyword=云计算&',
'https://www.shixiseng.com/interns/?keyword=土木&',
'https://www.shixiseng.com/interns/?keyword=物联网&',
'https://www.shixiseng.com/interns/?keyword=通信工程&',
'https://www.shixiseng.com/interns/?keyword=HR&',
'https://www.shixiseng.com/interns/?keyword=PS&',
'https://www.shixiseng.com/interns/?keyword=半导体&',
'https://www.shixiseng.com/interns/?keyword=新媒体&',
'https://www.shixiseng.com/interns/?keyword=嵌入式&',
'https://www.shixiseng.com/interns/?keyword=工商管理&',
'https://www.shixiseng.com/interns/?keyword=R语言&',
'https://www.shixiseng.com/interns/?keyword=产品经理&',
'https://www.shixiseng.com/interns/?keyword=电子商务&',
]

    rules = (
        Rule(LinkExtractor(allow='',restrict_xpaths=('//*[@class="title ellipsis font"]')), callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=('//*[@id="pagebar"]/ul/li[9]/a')))
    )

    def change(self,string):
        changedict = {
            '\ue5f4': '0', '\uf53e': '1', '\ue502': '2', '\uf3b3': '3', '\uf302': '4', '\ue3c9': '5', '\uf007': '6',
            '\uf614': '7', '\ue46f': '8', '\uf87d': '9'
        }
        for key, value in changedict.items():
            string = string.replace(key, value)
        return string

    def parse_item(self, response):
        item=ShixisengItem()
        item["job_name"]=response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/span/text()').extract_first()
        item["update_time"] = self.change(response.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/span[1]/text()').extract_first())
        item["salary"] = self.change(response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[1]/text()').extract_first())
        item["place"] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[2]/text()').extract_first()
        item["degree"] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[3]/text()').extract_first()
        item["weekly_time"] = self.change(response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[4]/text()').extract_first())
        item["total_time"] = self.change(response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[5]/text()').extract_first())
        tags= response.xpath('/html/body/div[1]/div[2]/div[1]/div[4]/span/text()').extract()
        list = []
        for i in tags:
            list.append(i)
        i_s1 = " ".join(list)
        item["tag"]=i_s1
        item["workplace"] = response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/span[1]/text()').extract_first()
        item["company"] = response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/a[2]/text()').extract_first()
        item["deadline"] = self.change(response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/text()').extract_first())
        item["url"] = response.url
        yield item
