import re
import scrapy
from scrapy import Spider
from scrapy.http.cookies import CookieJar
from scrapy import FormRequest,Request
from zhihu.settings import *

class Auth(Spider):
    name = 'auth'
    allowed_domains = ['zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    #start_urls = ['https://www.zhihu.com/settings/profile']

    def __init__(self):
        self.email = EMAIL
        self.password = PASSWORD
        self.cookiefile = 'cookies'
        self.p = re.compile('\<Cookie (.*?) for .zhihu.com\/\>')
        self.cookiejar = CookieJar()
        pass

    def post_login(self,response):
	xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
	print xsrf
	form = {account_type: self.email, "password": self.password, "remember_me": True }
	form['_xsrf'] = search_xsrf()
        return [FormRequest(url='http://www.zhihu.com/settings/profile',
                        meta = {'cookiejar':response.meta['cookiejar']},
                        headers = HEADER,
                        formdata={'_xsrf':xsrf,'email':self.email,'password':self.password},
                        callback=self.after_login)]

    def start_requests(self):
	cookiejar = ''
        with open(self.cookiefile,'r') as f:
                cookiejar = f.read()
        if cookiejar:
                cookies = re.findall(self.p, cookiejar)
                cookies = (cookie.split('=') for cookie in cookies)
                self.cookiejar = dict(cookies)
                return scrapy.Request('http://www.zhihu.com',
                        cookies=self.cookiejar,
                        callback = self.after_login)
        else:
		print 'start\n\n'
		return [Request("http://www.zhihu.com/login/email", meta = {'cookiejar':1}, callback = self.post_login)]

    def after_login(self,response):
        print response
        if 'authentication failed' in response.body:
        	print "login failed!"
                self.log('Login Failed',level=log.ERROR)
                return
        print "login successfully!"
        pass
