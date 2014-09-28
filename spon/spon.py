#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
from urllib2 import Request, urlopen, URLError
import urllib

def spon():
	schlagzeilen = open("news-spon.txt", "w+")
	request = Request('http://www.spiegel.de/schlagzeilen/')

	try:
		response = urlopen(request)
		html = response.read().decode('latin1')
	except URLError, e:
	    print 'Error:', e
	
#	find = re.findall('title="(.*?)\">', html)
	find = re.findall('<a href=\"(.*?)\".*?title="(.*?)\">', html)
			
	for a, i in find:
			#print http://www.spiegel.de + a #links
	  		if not "Newsletter" in i and not "Anzeige" in i and not "class" in i:
  				schlagzeilen.write(i.encode('utf-8') + "\n")
 
 	schlagzeilen.close()