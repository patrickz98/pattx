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

	find = re.findall(".*<strong>(.*?)</strong>.*?<em>(.*?)</em>.*", html)
	find2 = re.findall(".*?<em>(.*?)</em>.*", html)

	bla = []
	for a in find:
		schlagzeilen.write(str(a[0]) + ": " + str(a[1]) + "\n")
		bla.append(a[1])

	for b in find2:
		if b not in bla and len(b) > 15 and "SZ" not in b and "Bundesliga" not in b and "Kalender" not in b and "ueddeutsche" not in b:
			schlagzeilen.write(str(b) + "\n")

	schlagzeilen.close()
	regexhtml.main("news-sueddeutsche.txt")
