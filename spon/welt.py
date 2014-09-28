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
			find = re.search(".*?<a href=\"(.*?)\".*?<span>(.*?)</span>(.*?)</a>", a)
			#print find.group(1) links
			schlagzeilen.write(find.group(2) + " " + find.group(3) + "\n")


	schlagzeilen.close()
welt()