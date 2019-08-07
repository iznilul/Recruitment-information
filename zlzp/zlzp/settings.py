# -*- coding: utf-8 -*-

# Scrapy settings for zlzp project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zlzp'

SPIDER_MODULES = ['zlzp.spiders']
NEWSPIDER_MODULE = 'zlzp.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zlzp (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1.5
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16
# COOKIE={'sts_sg': '1', 'sts_sid': '16c14246cd635e-0560cce75a10fd-3c604504-2073600-16c14246cd75a2', 'loginreleased': '1', 'JsNewlogin': '3131040374', '__xsptplus30': '30.1.1540286385.1540286385.1%231%7C360PC%7CCPC%7Cjl%7C156070%7Cqg%23%23LaEEVwf474U5-HRZilE6VJO-7DPGX3Ff%23', 'adfcid': 'www.so.com', 'acw_tc': '2760825f15632798729731339e496ad0f9cc5f7d0eba08e84ac5b745b24dfd', 'sou_experiment': 'unexperiment', 'LastCity%5Fid': '765', 'JSpUserInfo': '386b2e69567146655f700169466d5d6a516b4177546f42355d75566b266925714a655e700669466d586a5c6b4077506f48355b755f6b5f69507124653b700869446d506a286b2577586f46354475596b4a695a71456555700769456d506a286b3d77586f41355275386b2b6956713d6526700169466d5d6a516b4177546f42355d755d6b51693e712365527004694e6d386a206b4c77556f4b359', 'rt': 'c12ceea1fbd1497f85acd212a0e71858', 'JSShowname': '', 'Hm_lvt_363368edd8b243d3ad4afde198719c4a': '1563363554,1563371161,1563419248,1563625661', 'urlfrom': '121122244', '__utmb': '269921210.1.10.1563706027', 'referrerUrl': 'https%3A//www.zhaopin.com/', 'adfcid2': 'www.so.com', 'adfbid': '0', 'stayTimeCookie': '1563706027376', 'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221043680124%22%2C%22%24device_id%22%3A%22166a03909b1194-02eabc3a2f140a-3c604504-2073600-166a03909b230c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2Fwww.so.com%2Flink%3Fm%3DaezXohAdMdgKAzqZ%252Fi9n7BmfXWVvnk8Y4FuCwjhCo70OiTnWGjK%252FMjkC5UBlV6Njup50ygcIEkG36cplNmI1Xb3UzlCeHCzlWAysFdobv%252FBo8slklwmjdkZro%252Fsw%253D%22%2C%22%24latest_referrer_host%22%3A%22www.so.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22360PC%22%2C%22%24latest_utm_medium%22%3A%22CPC%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22jn%22%2C%22%24latest_utm_term%22%3A%222316972%22%7D%2C%22first_id%22%3A%22166a03909b1194-02eabc3a2f140a-3c604504-2073600-166a03909b230c%22%7D', 'dywez': '95841923.1563706027.18.5.dywecsr', 'ZP_OLD_FLAG': 'false', 'dyweb': '95841923.1.10.1563706027', 'x-zp-client-id': '2030c8c3-4dbd-4339-86cc-c061ffe28b35', 'urlfrom2': '121122244', '__utmz': '269921210.1563706027.15.5.utmcsr', 'sts_chnlsid': 'Unknown', 'LastCity': '%E6%B7%B1%E5%9C%B3', 'Hm_lpvt_38ba284938d5eddca645bb5e02a02006': '1563706027', 'zp_src_url': 'http%3A%2F%2Fwww.so.com%2Flink%3Fm%3DaezXohAdMdgKAzqZ%252Fi9n7BmfXWVvnk8Y4FuCwjhCo70OiTnWGjK%252FMjkC5UBlV6Njup50ygcIEkG36cplNmI1Xb3UzlCeHCzlWAysFdobv%252FBo8slklwmjdkZro%252Fsw%253D', '__utmt': '1', '__utmc': '269921210', 'sts_deviceid': '166a0390773e1-0a9ab5f9f4718-3c604504-2073600-166a03907742be', '__utma': '269921210.1934485420.1540286385.1563625508.1563706027.15', 'at': 'd391510ba7024086889067b8f6534461', 'adfbid2': '0', 'dywec': '95841923', 'sts_evtseq': '1', 'JSloginnamecookie': '13335158225', 'dywea': '95841923.2013973910061177600.1540286384.1563626851.1563706027.18', 'uiioit': '3b622a64596409644764436a5b6e546e5c645438557756775e6855622c642064056447644c6a6', 'jobRiskWarning': 'true', 'Hm_lvt_38ba284938d5eddca645bb5e02a02006': '1563626466,1563626765,1563626863,1563706027'}
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zlzp.middlewares.ZlzpSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'zlzp.middlewares.RandomUserAgentMiddleware':543,
   'zlzp.middlewares.SeleniumDownloadMiddleware': 544,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zlzp.pipelines.AbroadwebsitePipeline': 300,
}
MYSQL_HOST='localhost'
MYSQL_DATABASE='spider'
MYSQL_ROOT='root'
MYSQL_PASSWORD='123'
USE='use spider'
TABLE='zlzp'
DROP="drop table if exists %s"%TABLE
CREATE='create table %s(job_name varchar(255) NOT NULL,salary varchar(255),want_numbers varchar(255),degree varchar(255),experience varchar(255),' \
       'update_time varchar(255),address varchar(255),workplace varchar(255),url varchar(255))'%TABLE
SAVEIN='insert into '+TABLE+' (job_name,salary,want_numbers,degree,experience,update_time,address,workplace,url) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
