import scrapy
from zhihu.settings import *
from scrapy import Spider
from scrapy import FormRequest,Request

class Followees(Spider):
	name = "followees"
	allowed_domains = ['zhihu.com']
	start_urls = ['http://www.zhihu.com/people/']

	def __init__(self):
		for url in start_urls:
			url += USER+'/followees'
				
		pass

	
