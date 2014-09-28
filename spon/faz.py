#!/usr/bin/python
import re
from urllib2 import Request, urlopen, URLError

def faz():
	schlagzeilen = open("news-faz.txt", "w+")
	request = Request('http://www.faz.net/')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall('<a title=\"(.*?)\" href=\"(.*?)\"', html)
	for i in find:
		if len(i[0]) > 15 and not "FAZ.NET-Comic-Roman" in i[0] and not "=" in i[0]:
# 			if "http://" in i[1]: 
# 				print i[1] 
# 			else: 
# 				print "http://www.faz.net/" + i[1]

			schlagzeilen.write(i[0] + "\n")


	schlagzeilen.close()
faz()