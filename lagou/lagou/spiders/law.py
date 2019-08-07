# -*- coding: utf-8 -*-
import scrapy
from lagou.items import *
from scrapy import Request

class LawSpider(scrapy.Spider):
    name = 'law'
    # allowed_domains = ['www.shit.com']
    start_urls = ['https://www.lagou.com/zhaopin/Java/',
'https://www.lagou.com/zhaopin/PHP/',
'https://www.lagou.com/zhaopin/C++/',
'https://www.lagou.com/zhaopin/qukuailian/',
'https://www.lagou.com/zhaopin/Android/',
'https://www.lagou.com/zhaopin/iOS/',
'https://www.lagou.com/zhaopin/shujuwajue/',
'https://www.lagou.com/zhaopin/shenduxuexi/',
'https://www.lagou.com/zhaopin/ziranyuyanchuli/',
'https://www.lagou.com/zhaopin/jiqixuexi/',
'https://www.lagou.com/zhaopin/ceshi/',
'https://www.lagou.com/zhaopin/html51/',
'https://www.lagou.com/zhaopin/jishuzongjian/',
'https://www.lagou.com/zhaopin/jiagoushi/',
'https://www.lagou.com/zhaopin/CTO/',
'https://www.lagou.com/zhaopin/chanpinzongjian/',
'https://www.lagou.com/zhaopin/chanpinjingli1/',
'https://www.lagou.com/zhaopin/shujuchanpinjingli/',
'https://www.lagou.com/zhaopin/youxicehua/',
'https://www.lagou.com/zhaopin/UIshejishi/',
'https://www.lagou.com/zhaopin/jiaohusheji/',
'https://www.lagou.com/zhaopin/wangyeshejishi/',
'https://www.lagou.com/zhaopin/pingmianshejishi/',
'https://www.lagou.com/zhaopin/shijueshejishi/',
'https://www.lagou.com/zhaopin/xinmeitiyunying/',
'https://www.lagou.com/zhaopin/bianji/',
'https://www.lagou.com/zhaopin/shujuyunying/',
'https://www.lagou.com/zhaopin/yunyingzongjian/',
'https://www.lagou.com/zhaopin/COO/',
'https://www.lagou.com/zhaopin/shichangshichangyingxiao1/',
'https://www.lagou.com/zhaopin/shichangtuiguang1/',
'https://www.lagou.com/zhaopin/shichangcehua1/',
'https://www.lagou.com/zhaopin/zhengfuguanxi1/',
'https://www.lagou.com/zhaopin/guanggaowenan/',
'https://www.lagou.com/zhaopin/guanggaotoufang/',
'https://www.lagou.com/zhaopin/shichangtuiguang1/',
'https://www.lagou.com/zhaopin/SEO1/',
'https://www.lagou.com/zhaopin/SEM1/',
'https://www.lagou.com/zhaopin/xiaoshouzhuanyuan1/',
'https://www.lagou.com/zhaopin/xiaoshoujingli1/',
'https://www.lagou.com/zhaopin/xiaoshouzongjian1/',
'https://www.lagou.com/zhaopin/xiaoshoudakehudaibiao/',
'https://www.lagou.com/zhaopin/kehujingli/',
'https://www.lagou.com/zhaopin/xiaoshoudianhuaxiaoshou/',
'https://www.lagou.com/zhaopin/HR/',
'https://www.lagou.com/zhaopin/xingzheng1/',
'https://www.lagou.com/zhaopin/caiwu1/',
'https://www.lagou.com/zhaopin/shenji/',
'https://www.lagou.com/zhaopin/xiaoyouxikaifa/',
'https://www.lagou.com/zhaopin/U3D/',
'https://www.lagou.com/zhaopin/youxicehua/',
'https://www.lagou.com/zhaopin/youxiyunying/',
'https://www.lagou.com/zhaopin/juqingsheji/',
'https://www.lagou.com/zhaopin/youxidonghua/',
'https://www.lagou.com/zhaopin/youxiyuanhua/',
'https://www.lagou.com/zhaopin/youxiyunying/',
'https://www.lagou.com/zhaopin/shouyoutuiguang/',
'https://www.lagou.com/zhaopin/youxizhuobo/',
'https://www.lagou.com/zhaopin/youxipeilian/',]

    def start_requests(self):
        for i in range(len(self.start_urls)):
           now_url=self.start_urls[i]
           yield Request(now_url,callback=self.get)

    def get(self,response):
        job_urls = response.xpath('//*[@class="position_link"]/@href').extract()
        for job_url in job_urls:
            yield Request(job_url, callback=self.parse)

    def parse(self, response):
        item = LagouItem()
        item["job_name"] = response.xpath('/html/body/div[4]/div/div[1]/div/h2/text()').extract_first()
        item["salary"] = response.xpath('/html/body/div[4]/div/div[1]/dd/h3/span[1]/text()').extract_first()
        item["place"] = response.xpath('/html/body/div[4]/div/div[1]/dd/h3/span[2]/text()').extract_first()
        item["experience"] = response.xpath('/html/body/div[4]/div/div[1]/dd/h3/span[3]/text()').extract_first()
        item["degree"] = response.xpath('/html/body/div[4]/div/div[1]/dd/h3/span[4]/text()').extract_first()
        item["category"] = response.xpath('/html/body/div[4]/div/div[1]/dd/h3/span[5]/text()').extract_first()
        item["update_time"] = response.xpath('/html/body/div[4]/div/div[1]/dd/p/text()').extract_first()
        tags = response.xpath('/html/body/div[4]/div/div[1]/dd/ul/li/text()').extract()
        list1 = []
        for i in tags:
            list1.append(i)
        i_s1 = " ".join(list1)
        item["tag"] = i_s1
        workplaces = response.xpath('//*[@id="job_detail"]/dd[3]/div[1]/a/text()').extract()
        list2 = []
        for i in workplaces:
            list2.append(i)
        i_s2 = " ".join(list2)
        item["workplace"] = i_s2
        addresses = response.xpath('//*[@id="job_detail"]/dd[3]/div[1]/text()').extract()
        list3 = []
        for i in addresses:
            list3.append(i)
        i_s3 = " ".join(list3)
        item["address"] = i_s3
        item["company"] = response.xpath('//*[@id="job_company"]/dt/a/div/h3/em/text()').extract_first()
        item["url"] = response.url
        yield item
        next=response.xpath('//*[@class="pager_container"]/a[last()]/@href')
        nexturl=response.urljoin(next)
        yield Request(nexturl,callback=self.get)
