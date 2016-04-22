import scrapy
from scrapy import Spider
from scrapy import FormRequest,Request
from settings import *
from items import ZhihuUserItem

class Auth(Spider):
	name = 'auth'
	allowed_domains = ['zhihu.com']
	start_urls = ['http://www.zhihu.com/']

	def __init__(self,usr=None):
		pass

	def post_login(self,response):
		xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
		#print xsrf
		return [FormRequest(url='http://www.zhihu.com/settings/profile',
		 	meta = {'cookiejar':response.meta['cookiejar']},
		  	headers = HEADER,
			formdata={'_xsrf':xsrf,'email':EMAIL,'password':PASSWORD},
			callback=self.after_login)]

	def start_requests(self):
		if COOKIE:
			return [Request('http://www.zhihu.com',
				meta = {'cookiejar': 1},
				headers = HEADER,
				cookies = COOKIE,
				callback = self.after_login)]
		else:
			return [Request("http://www.zhihu.com",
				headers = HEADER, 
				meta = {'cookiejar':1}, 
				callback = self.post_login)]

	def after_login(self,response):
		#print 'login successfully!'
		user = ZhihuUserItem()
		yield user
