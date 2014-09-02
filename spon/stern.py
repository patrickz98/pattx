#!/usr/bin/python
import os
import re
import regexhtml
from urllib2 import Request, urlopen, URLError

def stern():
	schlagzeilen = open("news-stern.txt", "w+")

	request = Request('http://www.stern.de/news/')

	try:
		response = urlopen(request)
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e
	
	last = ""	
	for a in html:
		if 'title=\"' in a and '<a href=' in a:
			find = re.search('title=\"(.*?)\">', a)
			if len(find.group(1)) > 18 and len(find.group(1)) < 110:
				if last != find.group(1):
					schlagzeilen.write(find.group(1) + "\n")
					last = find.group(1)
					
	schlagzeilen.close()
	regexhtml.main("news-stern.txt")
