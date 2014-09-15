#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
from collections import OrderedDict

import conf 
import regex
import blacklist
import spon, zeit, welt, stern, faz, ntv, tagesspiegel, sueddeutsche


spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
ntv.ntv()
tagesspiegel.tagesspiegel()
sueddeutsche.sueddeutsche()
regex.main()

dir = conf.dir
text = conf.text

html = open("aktuell.html", "w+")

def find(word):
	count = 0
	for txt in text:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				count = count + 1
	return count

result = []
def words():
	list = {}
	bad = blacklist.bad
	for txt in text:
		tx = open(txt, "r").readlines()
        
		for b in tx:
			for c in b.split():
				if ":" in c: c = c[:-1]
				if str(c) not in bad and c != "" and len(str(c)) > 3 or str(c) in blacklist.exception:
					if find(c) > 6:
						list.update({c:find(c)})
	
	html.write('<!doctype html>\n')
	html.write('<html>\n')
	html.write('	<head>\n')
	html.write('		<title>News Monitor</title>\n')
	html.write('		<link rel="icon" type="image/x-icon" href="news.ico" />\n')
	html.write('		<link rel="apple-touch-icon" href="news.png"/>')
	html.write('</head>\n')
	html.write('<body>\n')
	html.write('\n')
	html.write('		<h1>' 'Monitor: ' + time.strftime('%H:%M %d.%m.%Y') + '</h1>\n')
	html.write('\n')
	html.write('<p style="font-size:50px;"></p>')
	 
	
	for l in list:
		if list[l] >= 8 and l not in bad:
			html.write(('<p style="font-size:%dpx;">' % int(list[l] + 10)) + l + ': ' + str(list[l]) + '</p>\n')
	
	list = OrderedDict(sorted(list.items(), key=lambda x:x[1]))
	
	for l in reversed(list):
		if list[l] >= 8 and l not in bad:
			result.append(l + ": " + str(list[l]))

def data():
	try:
		os.mkdir(dir)
	except OSError:
		pass
	most = open(dir + time.strftime("%Y.%m.%d") + ".data", "w+")

	for a in result:
		most.write(a + "\n")
	
	most.close()
	
	schlagzeilen = open(dir + "news-" + time.strftime("%Y.%m.%d")+ ".txt", "w+")

	for txt in text:
		for lines in open(txt, "r").readlines():
			schlagzeilen.write(lines[:-1] + " (" + txt[5:-4] + ")" + "\n")
	
	schlagzeilen.close()

words()
data()