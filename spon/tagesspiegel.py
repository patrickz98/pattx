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
		if len(i[0]) > 15 and i[0] not in bla and "Tagesspiegel" not in i[0] and "Mediadaten" not in i[0] and "Sie haben Mut zur Uni" not in i[0]:
			#print "http://www.tagesspiegel.de/" + i[1] link
			schlagzeilen.write(i[0] + "\n")
			bla.append(i[0])

	schlagzeilen.close()
