def test():
	print 7
	yield 1
	yield 2
	yield 3
	print 4
	print 5
	print 6
	l = [{'_id': 'zhang-lan-emma','followees_num': u'25','info': [u'zengmin'],'nickname': u'\u5f20\u5c9a'}]
	l = str(l)
	import json
	print json.dumps(l)
test = test()
for item in test:
	print str(item) +" "+ str(item)
