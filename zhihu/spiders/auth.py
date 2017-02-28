import scrapy
from scrapy import Spider
from scrapy import FormRequest,Request
from settings import *
from items import ZhihuUserItem
#from zhihu.settings import *
#from zhihu.items import ZhihuUserItem
from scrapy.selector import Selector

class Auth(Spider):
	name = 'auth'
	allowed_domains = ['zhihu.com']
	start_urls = ['https://www.zhihu.com/']

	def __init__(self,usr=None):
		pass

	def post_login(self,response):
		xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
		#print xsrf
		return [FormRequest(url='https://www.zhihu.com/login/email',
			method='POST',
		 	meta = {'cookiejar':response.meta['cookiejar']},
			formdata={'_xsrf':xsrf,'email':EMAIL,'password':PASSWORD,'remember_me': 'true'},
			callback=self.after_login)]

	def start_requests(self):
		if COOKIE:
			print 'login with cookie'
			return [Request('https://www.zhihu.com',
				meta = {'cookiejar': 1},
				headers = HEADER,
				cookies = COOKIE,
				callback = self.after_login)]
		else:
			print 'login with password!'
			return [Request(#"https://www.zhihu.com",
				"https://www.zhihu.com/#signin",
				meta = {'cookiejar':1}, 
				callback = self.post_login)]

	def after_login(self,response):
		print 'login successfully!'
		user = ZhihuUserItem()
		yield user
