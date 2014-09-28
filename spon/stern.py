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
		html = response.read()
	except URLError, e:
	    print 'Error:', e
	
	last = ""	
	find = re.findall('<a href=\"(.*?)\".*?title=\"(.*?)\">', html)
	for a in find:
		if len(a[1]) > 18 and len(a[1]) < 110:
				#print a[0] links
 				if last != a[1]:
 					schlagzeilen.write(a[1] + "\n")
 					last = a[1]
					
	schlagzeilen.close()
	regexhtml.main("news-stern.txt")