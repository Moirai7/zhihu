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

USER = ['zhang-lan-emma']

HEADER={
    "Host": "www.zhihu.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36",
    "Referer": "http://www.zhihu.com/people/zhang-lan-emma",
    "Accept-Encoding": "gzip,deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-TW;q=0.2",
    }

COOKIE = {
	'udid': r'"ABAA1KtdmgmPTgosRMVfKY8dd719jXtmbtg=|1457758143"',
	'_za': r'9a88987b-04f3-4206-8e38-c4879a3b5c3a',
	'_zap': r'47d808a6-ff6a-4ddc-96c2-b05a806053ae',
	'_xsrf': r'2e10fcbd0bf407368d6165949638f933', 
	'd_c0': r'"ADBAjLNKoQmPTsWoA6NJ-Bea4ye0u_HGzZg=|1461058176"', 
	'l_n_c': r'1', 
	'q_c1': r'b71d8134388b40ffad0e874d8b9b9b01|1461131693000|1461131693000', 
	'cap_id': r'"NGVkNGVkOTM5ZDIwNDM5NmEzNmEyOTU1OGYyYzUzM2I=|1461131693|b8bb955c31c8fd2a78fa6500ae31800447684796"', 
	'l_cap_id': r'"Yjg3YmFkZWQyZmU5NDNjOWE5NmRlZmZjNDM1MGRhYWQ=|1461131693|7a4fb410b85a2cb3a9542232d1fe32c626620ceb"', 
	'__utmt':r'1',
 	'__utma':r'51854390.423555536.1461060097.1461118852.1461131697.5', 
	'__utmb':r'51854390.2.10.1461131697', 
	'__utmc':r'51854390', 
	'__utmz':r'51854390.1461118852.4.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)', 
	'__utmv':r'51854390.000--|2=registration_date=20130510=1^3=entry_date=20160420=1', 
	'login':r'"MjY1ZjhiZDNhZTVjNDllOWE4OWEzN2VjYTI3ZTJlZTQ=|1461131719|8a769ca3f1565d472bfe489ddc8df3baccfea9a6"', 
	'z_c0':r'"QUFCQWUwZ2JBQUFYQUFBQVlRSlZUYUtvUGxlLU5EckdTRmpNbjZneV9tRWdmbHA4a24xY0JRPT0=|1461132195|f677f59ae761b8c22b9e1500e78baafca159fb70"', 
	'unlock_ticket':r'"QUFCQWUwZ2JBQUFYQUFBQVlRSlZUYXNpRjFjUHJSRVpwdVFtaGxSVzZTSi1FdUhZeFFhWFJ3PT0=|1461132195|009bf1d876244c6bd290fac797d8462b85eccbb1"'
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
