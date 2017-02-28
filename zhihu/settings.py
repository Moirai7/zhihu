# -*- coding: utf-8 -*-

# Scrapy settings for zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhihu'

SPIDER_MODULES = ['zhihu.spiders']
NEWSPIDER_MODULE = 'zhihu.spiders'

EMAIL=['@gmail.com']
PASSWORD=['']

USER = 'zhang-lan-emma'

COOKIES_DEBUG = True

HEADER={
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Host': 'www.zhihu.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Accept': '*/*',
    'Origin': 'https://www.zhihu.com',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
}

COOKIE=False
''''
 {'d_c0'="ACBCXUvl5gqPThQCjf3Kxy07MchCyfq33Yc=|1480073838",
 '_zap'='a3c6fbd3-6af5-4f09-a2e0-15cf4ee8bac9', 
 'q_c1'='8d797744af7d4f339fc0df82c8f77dd0|1486051188000|1480073837000', 
 'aliyungf_tc'='AQAAACWr8RfeHAgA4tgFZUbctdVOuX85',
 '_xsrf'='e5a80179e72ecf5b7e25e96926c476b2'; 
 'l_cap_id'="YmE0ZTFhOTg1OTUyNDMwNmEzZWZiMDFjYjBlNThiOTI=|1488281281|84a8618fe495ab00c16fd2f26525bf63a54b293d", 'cap_id'="NmY4NzFjNGIzMzEyNDUxNmE0NjY4NGQxNTkxMWNhZDg=|1488281281|5ba34a421dfe7cce0ebcc67d63216ab5671e7a90", 'login'="M2IxMWMxNDM2NDNhNDcyZDkzNDY3NTk4MzE0ZjI3NzM=|1488281835|004d954362b856f8cdb32f392b6a11882818c865", 'nweb_qa'='heifetz', 'z_c0'='Mi4wQUFCQWUwZ2JBQUFBSUVKZFMtWG1DaGNBQUFCaEFsVk42LTNjV0FBMldqcWxPY3lZUFdpc3pncmZncmdGRldSZkRB|1488281837|42acd3e151526a20301ae8d6be04bc71f881ea1e', '__utma'='51854390.1651814320.1488277841.1488277841.1488281830.2', '__utmb'='51854390.0.10.1488281830', '__utmc'='51854390', '__utmz'='51854390.1488277841.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)', '__utmv'='51854390.100--|2=registration_date=20130510=1^3=entry_date=20130510=1'}

'''
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhihu (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhihu.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'zhihu.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
