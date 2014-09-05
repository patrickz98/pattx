#!/usr/bin/python
import re
from urllib2 import Request, urlopen, URLError

def spon():
	schlagzeilen = open("news-spon.txt", "w+")
	request = Request('http://www.spiegel.de/schlagzeilen/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall('title="(.*?)\">', html)

	for i in find:
			schlagzeilen.write(i + "\n")

	schlagzeilen.close()

spon()