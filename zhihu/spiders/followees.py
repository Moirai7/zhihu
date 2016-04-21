import scrapy
import json
from urllib import urlencode
from zhihu.settings import *
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider
from scrapy import FormRequest,Request
from zhihu.items import ZhihuUserItem

class Followees(CrawlSpider):
	name = "followees"
	allowed_domains = ['zhihu.com']

	def __init__(self):
		self.link = 'https://www.zhihu.com/people/'
		self.iters = 0
		self.check_name = []
		pass

	def start_requests(self):
		return [FormRequest('https://www.zhihu.com',
				meta = {'cookiejar': 1},
				headers = HEADER,
				cookies = COOKIE,
				callback = self.after_login)]

	def after_login(self,response):
		for url in USER:
			if url not in self.check_name:
				self.check_name.append(url)
			url = self.link + url + '/followees'
			return Request(url,headers = HEADER,cookies = COOKIE,callback=self.parse_user)
		pass

	def parse_user(self,response):
		print '\n'
		selector = Selector(text = response.body)
		user = ZhihuUserItem()
		user["_id"] = response.url.split('/')[-2]
		user["nickname"] = ''.join(selector.xpath("//div[@class='title-section ellipsis']/a[@class='name']/text()").extract())
		user["followees_num"] = ''.join(selector.xpath("//div[@class='zu-main-sidebar']/div[@class='zm-profile-side-following zg-clear']/a[@class='item'][1]/strong/text()").extract())
		user["info"]=[]

		print user["nickname"]
		_xsrf = ''.join(selector.xpath('//input[@name="_xsrf"]/@value').extract())
		#hash_id = ''.join(selector.xpath('//input[@name="dest_id"]/@value').extract())
		#hash_id = ''.join(selector.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())
		hash_id = ''.join(selector.xpath('//div[@class="body clearfix"]/form/input[@name="dest_id"]/@value').extract())
		if hash_id is None:
			hash_id = ''.join(selector.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())
		else:
			hash_id = "2171b0139e7cb85380aeb61b1e0abc58"
		print "hash_id : "+hash_id
		#hash_id = "2171b0139e7cb85380aeb61b1e0abc58"

		num = int(user["followees_num"]) if user["followees_num"] else 0
		page_num = num/20
		page_num += 1 if num%20 else 0
		for i in xrange(page_num):
			params = json.dumps({"hash_id":hash_id,"order_by":"created","offset":i*20})
			payload = {"method":"next", "params": params, "_xsrf":_xsrf}

			#firstly i dont understant why i should use request not formrequest,actually,it's a post method.
			#secondly it's weird that if i'm not use yield, the callback function wont be called.
			#finally i dont know why i use the return value to call the callback function wont get a right reponse value.

			#yield FormRequest('https://www.zhihu.com/node/ProfileFolloweesListV2',formdata=payload,headers = HEADER,cookies = COOKIE,callback = self.parse_followees_id,meta={"item":user})
			yield Request("https://www.zhihu.com/node/ProfileFolloweesListV2?"+urlencode(payload),headers = HEADER,cookies = COOKIE,callback=self.parse_followees_id,meta={"item":user})

		print user["info"]
		if self.iters < 7:
			for username_tmp in user["info"]:
				if username_tmp not in self.check_name:
					self.check_name.append(username_tmp)
					yield Request(self.link+username_tmp+"/followees", callback=self.parse_user)
		self.iters += 1
		yield user
		
	def parse_followees_id(self,response):
		user = response.meta['item']
		selector = Selector(text = response.body)
		#user = []
		for link in selector.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract():
			username_tmp = link.split('/')[-1]
			#if username_tmp in self.user_names:
			#	print 'GET:' + '%s' % username_tmp
			#	continue
			user["info"].append(username_tmp)
		return user
