#!/usr/bin/python
import os
import re
from urllib2 import Request, urlopen, URLError

def welt():
	schlagzeilen = open("news-welt.txt", "w+")
	request = Request('http://www.welt.de/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall(".*?<a href=\"(.*?)\".*?<span>(.*?)</span>(.*?)</a>", html)
	for i in find:
		#print i
		schlagzeilen.write(i[1] + " " + i[2] + "\n")


	schlagzeilen.close()
