#!/usr/bin/python
import re
from urllib2 import Request, urlopen, URLError

def zeit():
	schlagzeilen = open("news-zeit.txt", "w+")
	request = Request('http://www.zeit.de/news/index')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall("<strong>(.*?)</strong> <span>(.*?)</span>", html)

	for i in find:
			schlagzeilen.write(i[0] + ": " + i[1] + "\n")

	schlagzeilen.close()
