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
from scrapy.http.cookies import CookieJar
import re

class Followees(CrawlSpider):
	name = "followees"
	allowed_domains = ['zhihu.com']

	def __init__(self,users=None):
		if users is None:
			self.users = USER
		else:
			self.users = users

		self.cookie_file = 'cookie'
		self.link = 'https://www.zhihu.com/people/'
		pass

	def post_login(self,response):
                self.xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
                return [FormRequest(url='https://www.zhihu.com/login/email',
                        method='POST',
			headers = HEADER,
                        meta = {'cookiejar':response.meta['cookiejar']},
                        formdata={'_xsrf':self.xsrf,'email':EMAIL,'password':PASSWORD},
                        callback=self.after_login)]

        def start_requests(self):
		with open(self.cookie_file) as f:
                        cookiejar = f.read()
                        p = re.compile('\<Cookie (.*?) for .zhihu.com\/\>')
                        cookies = re.findall(p, cookiejar)
                        #cookies = (cookie.split('=') for cookie in cookies)
                        mcookies = []
                        for cookie in cookies:
                                lists = cookie.split('=')
                                mcookies.append((lists[0],'='.join(lists[1:len(lists)])))
                        COOKIE = dict(mcookies)
		cookie_jar = CookieJar()
                if COOKIE is not False:
			print 'login with cookie!'
                        return [Request('https://www.zhihu.com',
                                meta = {'cookiejar': cookie_jar},
                                headers = HEADER,
                                cookies = COOKIE,
                                callback = self.after_login)]
                else:
			print 'login with password!'
                        return [Request("https://www.zhihu.com/#signin",
                                meta = {'dont_merge_cookies': True, 'cookiejar': cookie_jar},
				headers = HEADER,
                                callback = self.post_login)]

        def after_login(self,response):
                print 'login successfully!'
		url = self.link + self.users + '/following'
		#url = self.link + self.users + '/followers'
		
		if COOKIE:
			return [Request(url,meta={'cookiejar': response.meta['cookiejar']},headers = HEADER,cookies = COOKIE,callback=self.parse_user)]
		else:
			cookie_jar = response.meta['cookiejar']
			cookie_jar.extract_cookies(response, response.request)
			with open(self.cookie_file, 'wb+') as f:
				for cookie in cookie_jar:
					f.write(str(cookie) + '\n')
			return [Request(url,meta={'cookiejar': response.meta['cookiejar']},callback=self.parse_user,headers=HEADER)]

	def parse_user(self,response):
		selector = Selector(text = response.body)
		print response.body
		user = ZhihuUserItem()
		user["_id"] = response.url.split('/')[-2]
		user["nickname"] = ''.join(selector.xpath("//span[@class='ProfileHeader-name']/text()").extract())
		user["followings_num"] = ''.join(selector.xpath("//div[@class='NumberBoard FollowshipCard-counts']/a[1]/div[@class='NumberBoard-value']/text()").extract())
		user["followers_num"] = ''.join(selector.xpath("//div[@class='NumberBoard FollowshipCard-counts']/a[2]/div[@class='NumberBoard-value']/text()").extract())
		user["info"]=[]

		num = int(user["followings_num"]) if user["followings_num"] else 0
		print user["nickname"].encode('utf-8')
		i = 0
		while i<num:
			_url = 'https://www.zhihu.com/api/v4/members/'+user["_id"]+'/followees?include=data%5B*%5D.C&offset='+str(i)+'&limit='+str(i+20)
			i += 20
			if COOKIE is not False:
				yield Request(_url,callback = self.parse_followings_id,meta={"item":user},headers=HEADER,cookies=COOKIE)
			else:
				yield Request(_url,callback = self.parse_followings_id,meta={'cookiejar': response.meta['cookiejar'],"item":user},headers=HEADER)
		'''
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
		'''
		yield user

	def parse_followings_id(self,response):
		print response.body
		body = json.loads(response.body)
		user = response.meta['item']
		for link in body['data']:
			username_tmp = link['url_token']
			user["info"].append(username_tmp)
		return user
		'''	
		user = response.meta['item']
		#selector = Selector(text = response.body)
		selector = Selector(response)
		for link in selector.xpath("//div[@class='UserItem-title']/span/div/div/a/@href").extract():
			username_tmp = link.split('/')[-1]
			user["info"].append(username_tmp)
		#yield user
		return user
		'''
