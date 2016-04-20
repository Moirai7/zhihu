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
		pass

	def start_requests(self):
		return [FormRequest('http://www.zhihu.com',
				meta = {'cookiejar': 1},
				headers = HEADER,
				cookies = COOKIE,
				callback = self.after_login)]

	def after_login(self,response):
		for url in USER:
			url = self.link + url + '/followees'
			yield Request(url,headers = HEADER,cookies = COOKIE,callback=self.parse_user)
		pass

	def parse_user(self,response):
		print '\n'
		print response.url
		selector = Selector(text = response.body)
		user = ZhihuUserItem()
		user["_id"] = response.url.split('/')[-2]
		user["nickname"] = ''.join(selector.xpath("//div[@class='title-section ellipsis']/a[@class='name']/text()").extract())
		user["followees_num"] = ''.join(selector.xpath("//div[@class='zu-main-sidebar']/div[@class='zm-profile-side-following zg-clear']/a[@class='item'][1]/strong/text()").extract())
		user["info"]=[]

		print user["_id"]
		print user["nickname"]
		print user["followees_num"]
		_xsrf = ''.join(selector.xpath('//input[@name="_xsrf"]/@value').extract())
		hash_id = ''.join(selector.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())
		
		num = int(user["followees_num"]) if user["followees_num"] else 0
		page_num = num/20
		page_num += 1 if num%20 else 0
		for i in xrange(page_num):
			params = json.dumps({"hash_id":hash_id,"order_by":"created","offset":i*20})
			payload = {"method":"next", "params": params, "_xsrf":_xsrf}

			ajax = Request("http://www.zhihu.com/node/ProfileFolloweesListV2?"+urlencode(payload),callback=self.parse_follow_url)
			#print ajax.body
			
			#ajax = Request("https://www.zhihu.com/node/ProfileFolloweesListV2?"+urlencode(payload),headers = HEADER,cookies = COOKIE)
			#print ajax.body
			ajax.meta['item'] = user
			#self.parse_follow_url(request)
		
		
		#return Request(self.link+url+"/followees", callback=self.parse_user)
		yield user
		
	def parse_follow_url(self,response):
		print response.url
		print response.headers
		print response.body
		
		item = response.meta['item']
		selector = Selector(text = response.body)
		for link in selector.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract():
			username_tmp = link.split('/')[-1]
			#if username_tmp in self.user_names:
			#	print 'GET:' + '%s' % username_tmp
			#	continue
			print username_tmp
			item['info'].append(username_tmp)
			raw_input( )
		return item
