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

EMAIL=['moirai.zhang@gmail.com']
PASSWORD=['moirai742612']

HEADER={
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Referer": "http://www.zhihu.com/people/raymond-wang",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    }

COOKIE={
	"udid":r"ABAA1KtdmgmPTgosRMVfKY8dd719jXtmbtg=|1457758143",
	"_za":r"9a88987b-04f3-4206-8e38-c4879a3b5c3a", 
	"_zap":r"47d808a6-ff6a-4ddc-96c2-b05a806053ae", 
	"q_c1":r"d87e684d1f6f4163ab438f45a482a14c|1460423049000|1457754748000", 
	"_xsrf":r"2e10fcbd0bf407368d6165949638f933", 
	"d_c0":r"ADBAjLNKoQmPTsWoA6NJ-Bea4ye0u_HGzZg=|1461058176", 
	"l_n_c":r"1", 
	"__utma":r"51854390.423555536.1461060097.1461114203.1461116115.3",
 	"__utmb":r"51854390.4.10.1461116115", 
	"__utmc":r"51854390", 
	"__utmz":r"51854390.1461060097.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/40291772", 
	"__utmv":r"51854390.000--|3=entry_date=20160312=1", 
	"login":r"ZTA2YjIzMTI2MTUyNGJkMzk0NjE3N2VjNGRhNjY4NzI=|1461116946|43e01c137f6612fa617a051d85c274fa68c7ff20", 
	"l_cap_id":r"OWZiODJlYzE5YTk1NGZiNDhjYTE0YjQ5YWE0NmNjOWE=|1461116946|744c25393ee299bc91900f059bb3b619ed432281", 
	"cap_id":r"NTRjOGY0ZGIyY2IyNGU2ZDg5YTI4MDAwOWE3OTQ2NWM=|1461116946|018530d2769f4f30e3d04e9a041c21c628cca259", 
	"z_c0":r"QUFCQWUwZ2JBQUFYQUFBQVlRSlZUUmx0UGxlajBycWdHbkIzVlI2V2dDekdpMW5nanZwaGlBPT0=|1461116953|d3734806b865cc583acdd7438fd6f9e4593132ac", 
	"unlock_ticket":r"QUFCQWUwZ2JBQUFYQUFBQVlRSlZUU0huRmxjZ3lrNVJ0OGsxb2l0dEdIZWJoa1VSRlo2Nm5nPT0=|1461116953|be386db37d8f4c87d6d4e9d71594991b8b996f4c"
}


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
