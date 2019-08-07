# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
from lagou.settings import *
import pymysql
from scrapy import signals
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
from scrapy.http.response.html import HtmlResponse
from selenium import webdriver
import time
import random
# class SeleniumDownloadMiddleware(object):
#     def __init__(self):
#         self.driver = webdriver.Chrome(chrome_options=chrome_options)
#         # self.driver = webdriver.Chrome()
#     def process_request(self, request, spider):
#         self.driver.get(request.url)
#         time.sleep(0.3)
#         try:
#             button = self.driver.find_element_by_xpath('//*[@class="pager_next "]')
#             button.click()
#         except:
#             pass
#         time.sleep(0.5)
#         source = self.driver.page_source
#         response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding='utf-8')
#         return response
class RandomUserAgentMiddleware():
    def __init__(self):
        self.user_agents=[
            "Mozilla/5.0(Windows;U;MSIE 9.0;Windows NT 9.0; en-US)",
            "Mozilla/5.0(Windows NT 6.1)AppleWebKit/537.2(KHTML,like Gecko)Chrome/22.0.1216.0 Safari/537.2",
            "Mozilla/5.0(X11;Ubuntu;Linux i686;rv:15.0)Gecko/20100101 Firefox/15.0.1",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
                "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
                "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
                "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
                "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
                "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
                "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        ]
        # self.cookie={'privacyPolicyPopup': 'false', 'PRE_HOST': 'www.so.com', 'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1563534241', 'X_MIDDLE_TOKEN': 'd762f711b5dc42acfed6c33bcea554b8', 'PRE_SITE': 'https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3Dhao_360so_b%26shb%3D1%26hsid%3D518413bf23c15e75%26q%3D%25E6%258B%2589%25E9%2592%25A9', 'LGSID': '20190719183636-15933f06-aa11-11e9-810b-525400f775ce', 'login': 'true', 'gate_login_token': '6986bcd53843b47667511c2e02e7083708cff7e4d1c253f9c1265a9d186ea48b', 'LGUID': '20190711202242-947940bf-a3d6-11e9-a4de-5254005c3644', 'SEARCH_ID': '5412d292644a426a99017bc8bb1142ae', 'user_trace_token': '20190711202240-5d0243d5-6068-4ccf-8a07-a2584d36e0d6', '_gat': '1', '_putrc': '541AC90E5B191B34123F89F2B170EADC', '_ga': 'GA1.2.1153318529.1562847761', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2216c094a965d27-0c74e35a93291-3c604504-2073600-16c094a965e68a%22%2C%22%24device_id%22%3A%2216c094a965d27-0c74e35a93291-3c604504-2073600-16c094a965e68a%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D', 'hasDeliver': '0', 'X_HTTP_TOKEN': '4c1f5695297129b51424353651b8468d3b50b3d6dc', 'PRE_UTM': '', 'LGRID': '20190719190402-ea7c1e73-aa14-11e9-a4e9-5254005c3644', 'JSESSIONID': 'ABAAABAAAIAACBI2A91F0C7368F35CE7E47D4E1BFE7B27E', 'index_location_city': '%E5%85%A8%E5%9B%BD', 'TG-TRACK-CODE': 'index_search', 'unick': '%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B78225', 'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1563521291,1563531487,1563532595,1563534140', 'sajssdk_2015_cross_new_user': '1', '_gid': 'GA1.2.1775814610.1563520358', 'PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2F'}
    def process_request(self,request,spider):
        request.headers["User-Agent"]=random.choice(self.user_agents)
class ProxyMiddleware1():
    def __init__(self):
        self.PROXIES =[]
        self.connect = pymysql.connect(MYSQL_HOST, MYSQL_ROOT, MYSQL_PASSWORD, MYSQL_DATABASE)
        self.cursor = self.connect.cursor()
        self.cursor.execute(USE)
        self.cursor.execute(SQL)
        alldata = self.cursor.fetchall()
        for data in alldata:
            self.PROXIES.append(data)
        self.cursor.execute(SQL2)
        alldata1=self.cursor.fetchall()
        for data in alldata:
            self.PROXIES.append(data)
    def process_request(self, request, spider):
        proxy = random.choice(self.PROXIES)
        request.meta['proxy'] ="http://"+proxy[0]

class ProxyMiddleware2():
    def __init__(self):
        self.PROXIES =[]
        self.connect = pymysql.connect(MYSQL_HOST, MYSQL_ROOT, MYSQL_PASSWORD, MYSQL_DATABASE)
        self.cursor = self.connect.cursor()
        self.cursor.execute(USE)
        self.cursor.execute(SQL1)
        alldata = self.cursor.fetchall()
        for data in alldata:
            self.PROXIES.append(data)
    def process_request(self, request, spider):
        proxy = random.choice(self.PROXIES)
        request.meta['proxy'] = proxy[0]+"://"+proxy[1]

class LagouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class LagouDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
