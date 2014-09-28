#!/usr/bin/python
import os
import re
import regexhtml
from urllib2 import Request, urlopen, URLError

def sueddeutsche():
	schlagzeilen = open("news-sueddeutsche.txt", "w+")
	request = Request('http://www.sueddeutsche.de/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall("<a href=\"(.*?)\".*?<strong>(.*?)</strong>.*?<em>(.*?)</em>.*", html)
	find2 = re.findall("<a href=\"(.*?)\".*?<em>(.*?)</em>.*", html)

	bla = []
	for a in find:
		#print a[0] links
		schlagzeilen.write(str(a[1]) + ": " + str(a[2]) + "\n")
		bla.append(a[2])

	for b in find2:
		#print b[1] links
		if b[1] not in bla and len(b[1]) > 10 and "SZ" not in b[1] and "Bundesliga" not in b[1] and "Kalender" not in b[1] and "ueddeutsche" not in b[1]:
			schlagzeilen.write(str(b[1]) + "\n")

	schlagzeilen.close()
	regexhtml.main("news-sueddeutsche.txt")
