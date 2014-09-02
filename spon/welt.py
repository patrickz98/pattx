#!/usr/bin/python
import os
import re
from urllib2 import Request, urlopen, URLError

def welt():
	schlagzeilen = open("news-welt.txt", "w+")
	request = Request('http://www.welt.de/')

	try:
		response = urlopen(request)
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e

	for a in html:
		if "<h4>" in a and "<span>" in a:
			find = re.search("<span>(.*?)</span>(.*?)</a>", a)
			schlagzeilen.write(find.group(1) + " " + find.group(2) + "\n")


	schlagzeilen.close()