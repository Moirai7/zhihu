from multiprocessing import Process
from multiprocessing.queues import Queue
from spiders.followees import Followees
from spiders.auth import Auth
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from scrapy.crawler import CrawlerProcess,Crawler
from scrapy.settings import Settings
import json

class CrawlerWorker(Process):
    def __init__(self, spider,query,results):
        Process.__init__(self)
        self.results = results
        self.items = []
        self.query = query
        self.spider = spider
        dispatcher.connect(self._item_passed, signals.item_passed)

    def _item_passed(self, item):
        self.items.append(item)

    def run(self):
        #self.crawler = CrawlerProcess(get_project_settings())
        self.crawler = CrawlerProcess(Settings())
        self.crawler.crawl(self.spider,self.query)
        self.crawler.start()
        self.crawler.stop()
	if len(self.items)>0:
		print json.dumps(dict(self.items[0]))
        	self.results.put(self.items[0])
	else:
        	self.results.put(self.query)

if __name__ == '__main__':
    #results = Queue()
    #crawler = CrawlerWorker(Auth(),'zhang-lan-emma',results)
    #crawler.start()

    results = Queue()
    check_name = []
    check_name.append('zhang-lan-emma')
    crawler = CrawlerWorker(Followees(),'zhang-lan-emma',results)
    crawler.start()
    users =[]
    users.append(results.get())
   
    iters = 0 
    while iters < 7:
	for user in users:
		for username_tmp in user["info"]:
			if username_tmp not in check_name:
				check_name.append(username_tmp)
    				results = Queue()
				crawler = CrawlerWorker(Followees(),username_tmp,results)
				crawler.start()
				users.append(results.get())
    	iters += 1
    print json.dumps(users)
