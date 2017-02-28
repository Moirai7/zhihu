# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ZhihuUserItem(scrapy.Item):
	_id = scrapy.Field()
	nickname = scrapy.Field()
	followings_num = scrapy.Field()
	followers_num = scrapy.Field()
	info = scrapy.Field()

class ZhihuInfoItem(scrapy.Item):
	school = scrapy.Field()
	work = scrapy.Field()
	agree_num = scrapy.Field()
	thx_num = scrapy.Field()
	ask_num = scrapy.Field()
	ans_num = scrapy.Field()
	paper_num = scrapy.Field()
	collect_num = scrapy.Field()

