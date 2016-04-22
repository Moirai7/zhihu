import scrapy
import json
from urllib import urlencode
#from zhihu.settings import *
#from zhihu.items import ZhihuUserItem
from items import ZhihuUserItem
from settings import *
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider
from scrapy import FormRequest,Request

class Followees(CrawlSpider):
	name = "followees"
	allowed_domains = ['zhihu.com']

	def __init__(self,users=None):
		if users is None:
			self.users = USER
		else:
			self.users = users
		self.link = 'https://www.zhihu.com/people/'
		pass

	def start_requests(self):
	#	return [FormRequest('https://www.zhihu.com',
	#			meta = {'cookiejar': 1},
	#			headers = HEADER,
	#			cookies = COOKIE,
	#			callback = self.after_login)]

	#def after_login(self,response):
		url = self.link + self.users + '/followees'
		return [Request(url,headers = HEADER,cookies = COOKIE,callback=self.parse_user)]

	def parse_user(self,response):
		#print '\n'
		selector = Selector(text = response.body)
		user = ZhihuUserItem()
		user["_id"] = response.url.split('/')[-2]
		user["nickname"] = ''.join(selector.xpath("//div[@class='title-section ellipsis']/a[@class='name']/text()").extract())
		user["followees_num"] = ''.join(selector.xpath("//div[@class='zu-main-sidebar']/div[@class='zm-profile-side-following zg-clear']/a[@class='item'][1]/strong/text()").extract())
		user["info"]=[]

		#print user["nickname"].encode('utf-8')
		_xsrf = ''.join(selector.xpath('//input[@name="_xsrf"]/@value').extract())
		#hash_id = ''.join(selector.xpath('//div[@class="zm-profile-header-op-btns clearfix"]/button/@data-id').extract())
		#if hash_id is None:
		#	hash_id = ''.join(selector.xpath('//div[@class="body clearfix"]/form/input[@name="dest_id"]/@value').extract())
		data_init = json.loads(''.join(selector.xpath('//div[@class="zh-general-list clearfix"]/@data-init').extract()))
		hash_id = data_init["params"]["hash_id"]
		#print "hash_id : "+hash_id

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

		yield user
		
	def parse_followees_id(self,response):
		user = response.meta['item']
		selector = Selector(text = response.body)
		for link in selector.xpath('//div[@class="zm-list-content-medium"]/h2/a/@href').extract():
			username_tmp = link.split('/')[-1]
			user["info"].append(username_tmp)
		return user
