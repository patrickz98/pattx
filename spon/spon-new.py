#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from urllib2 import Request, urlopen, URLError
import unicodedata as ucd

def spon():
	schlagzeilen = open("news-spon.txt", "w+")
	request = Request('http://www.spiegel.de/schlagzeilen/')

	try:
		response = urlopen(request)
		html = response.read()
		html = unicode(html.decode('UTF8'))
	except URLError, e:
	    print 'Error:', e
	
#	find = re.findall('<a href=\"(.*?)\".*?title="(.*?)\">', html)
	find = re.findall('title="(.*?)\">', html)
			
	for i in find:
  		if not "Newsletter" in i and not "Anzeige" in i:
  			print i
 			schlagzeilen.write(i + "\n")

	schlagzeilen.close()
spon()