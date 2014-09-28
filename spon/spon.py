#!/usr/bin/python
import os
from urllib2 import Request, urlopen, URLError
import re

import regexspon

def spon():
	schlagzeilen = open("news-spon.txt", "w+")
	request = Request('http://www.spiegel.de/schlagzeilen/')

	try:
		response = urlopen(request)
		html = response.readlines()
	except URLError, e:
	    print 'Error:', e

	raw = str([x for x in html if "title=" in x])

	tit = raw
	title = []

	while(True):
		if tit.find('title=') and not tit.find('title=') == -1:
			part1 = tit.find('title=') + 7
			part2 = tit.find('>')
	        	t = str(tit[part1:part2 - 1])

			title.append(str(tit[part1:part2 - 1]))
			tit = tit[part2 + 1:]
		else:
			break

	write = []
	for t in title:
		if len(t) >= 8 and not 'Anzeige' in t and not 'nav-channel-name' in t and not 'SPIEGEL ONLINE' in t:
			schlagzeilen.write(t + "\n")
			write.append(t)


	schlagzeilen.close()
	regexspon.main()
spon()