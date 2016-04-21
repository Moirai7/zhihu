def test():
	print 7
	yield 1
	yield 2
	yield 3
	print 4
	print 5
	print 6
test = test()
for item in test:
	print str(item) +" "+ str(item)
