#!/usr/bin/python
import os
import re
from urllib2 import Request, urlopen, URLError

def zeit():
	schlagzeilen = open("news-zeit.txt", "w+")
	request = Request('http://www.zeit.de/news/index')

	try:
		response = urlopen(request)
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e

	last = ""
	for a in html:
		if "<span>" in a and "<strong>" in a:
			find = re.search("<strong>(.*?)</strong> <span>(.*?)</span>", a)
#			print find.group(1)[6:-7]
			if last != find.group(1) + ": " + find.group(2) + "\n":
				schlagzeilen.write(find.group(1) + ": " + find.group(2) + "\n")
				last = find.group(1) + ": " + find.group(2) + "\n"

	schlagzeilen.close()
