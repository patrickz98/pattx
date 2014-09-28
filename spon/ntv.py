#!/usr/bin/python
import os
import re
from urllib2 import Request, urlopen, URLError

import regexntv

def ntv():
	schlagzeilen = open("news-ntv.txt", "w+")
	request = Request('http://www.n-tv.de/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall('.*?<a href="(.*?)" title="(.*?)">', html)

	for i in find:
		if not "=" in i[1] and not "\"" in i[1]:
			#if not "=" in i[0]: print i[0]
			schlagzeilen.write(i[1] + "\n")


	schlagzeilen.close()
