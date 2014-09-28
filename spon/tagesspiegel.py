#!/usr/bin/python
import os
import re
from urllib2 import Request, urlopen, URLError

def tagesspiegel():
	schlagzeilen = open("news-tagesspiegel.txt", "w+")
	request = Request('http://www.tagesspiegel.de/schlagzeilen/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall('<a title=\"(.*?)\".*?href=\"(.*?)\"', html)
	bla = []

	for i in find:
		if len(i) > 15 and i not in bla and "Tagesspiegel" not in i and "Mediadaten" not in i and "Sie haben Mut zur Uni" not in i:
			#print "http://www.tagesspiegel.de/" + i[1] link
			schlagzeilen.write(i[0] + "\n")
			bla.append(i[0])

	schlagzeilen.close()
