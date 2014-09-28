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

	find = re.findall("<a href=\"(.*?)\".*?<strong>(.*?)</strong> <span>(.*?)</span>", html)

	for i in find:
			#print i[0] link
			schlagzeilen.write(i[1] + ": " + i[2] + "\n")

	schlagzeilen.close()
