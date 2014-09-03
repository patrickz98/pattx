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
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e

	safe = ""
	for a in html:
		if "<span class=\"" in a and "</span>" in a:
			find = re.search('<span class=.*?>(.*?)</span>', a)
			schlagzeilen.write(find.group(1) + "\n")


	schlagzeilen.close()
	regexntv.main()