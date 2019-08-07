# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from shixiseng.items import *
from scrapy import Request
class SxswSpider(scrapy.Spider):
    name = 'sxsw'
    # allowed_domains = ['www.shit.com']
    page=50
    start_urls = ['https://www.shixiseng.com/interns/?keyword=Java&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=UI设计师&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=Web前端&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=PHP&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=Python&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=Android&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=美工&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=深度学习&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=算法工程师&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=Hadoop&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=Node.js&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=数据开发&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=数据分析师&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=数据架构&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=人工智能&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=区块链&degree=&enterprise=&salary-=0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=电气工程&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=销售&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=金融&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=英语&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=数据挖掘&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=云计算&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=土木&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=物联网&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=通信工程&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=HR&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=PS&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=半导体&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=新媒体&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=嵌入式&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=工商管理&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=R语言&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=产品经理&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',
'https://www.shixiseng.com/interns/?keyword=电子商务&degree=&enterprise=&salary=-0&publishTime=&offiacal=&type=intern&sortType=&city=%E5%85%A8%E5%9B%BD&months=&days=&',]

    def change(self,string):
        changedict = {
            '\ue5f4': '0', '\uf53e': '1', '\ue502': '2', '\uf3b3': '3', '\uf302': '4', '\ue3c9': '5', '\uf007': '6',
            '\uf614': '7', '\ue46f': '8', '\uf87d': '9'
        }
        for key, value in changedict.items():
            string = string.replace(key, value)
        return string

    def start_requests(self):
        for i in range(len(self.start_urls)):
           now_url=self.start_urls[i]
           for s in range(self.page):
               data = {
                   "page": s+1,
               }
               params = urlencode(data)
               new_url=now_url+params
               yield Request(new_url,callback=self.get)
    def get(self,response):
        job_urls=response.xpath('//*[@class="title ellipsis font"]/@href').extract()
        for job_url in job_urls:
            yield Request(job_url,callback=self.parse)
    def parse(self, response):
        item = ShixisengItem()
        item["job_name"] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/span/text()').extract_first()
        item["update_time"] = self.change(
            response.xpath('/html/body/div[1]/div[2]/div[1]/div[2]/span[1]/text()').extract_first())
        item["salary"] = self.change(
            response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[1]/text()').extract_first())
        item["place"] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[2]/text()').extract_first()
        item["degree"] = response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[3]/text()').extract_first()
        item["weekly_time"] = self.change(
            response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[4]/text()').extract_first())
        item["total_time"] = self.change(
            response.xpath('/html/body/div[1]/div[2]/div[1]/div[3]/span[5]/text()').extract_first())
        tags = response.xpath('/html/body/div[1]/div[2]/div[1]/div[4]/span/text()').extract()
        list = []
        for i in tags:
            list.append(i)
        i_s1 = " ".join(list)
        item["tag"] = i_s1
        item["workplace"] = response.xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/span[1]/text()').extract_first()
        item["company"] = response.xpath(
            '/html/body/div[1]/div[2]/div[2]/div[1]/div[4]/div[2]/a[2]/text()').extract_first()
        item["deadline"] = self.change(
            response.xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/div[3]/text()').extract_first())
        item["url"] = response.url
        yield item
