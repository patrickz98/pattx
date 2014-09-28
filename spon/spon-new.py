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
	except URLError, e:
	    print 'Error:', e
	
#	find = re.findall('<a href=\"(.*?)\".*?title="(.*?)\">', html)
	find = re.findall('title="(.*?)\">', html)
			
	for i in find:
		print i.decode('latin1')
#  		if not "Newsletter" in i:
#  			try:
#  				i = i.encode('latin1')
#  				schlagzeilen.write(i + "\n")
#  			except:
# 				pass

	schlagzeilen.close()
spon()