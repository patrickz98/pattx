#!/usr/bin/python
import re
from urllib2 import Request, urlopen, URLError

def faz():
	schlagzeilen = open("news-faz.txt", "w+")
	request = Request('http://www.faz.net/')

	try:
		response = urlopen(request)
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e

	for a in html:
		if '<a title=' in a:
			find = re.search('<a title=\"(.*?)\"', a)
			if len(find.group(1)) > 15 and not "FAZ.NET-Comic-Roman" in find.group(1):
				schlagzeilen.write(find.group(1) + "\n")


	schlagzeilen.close()
