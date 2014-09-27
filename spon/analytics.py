#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
from collections import OrderedDict

import mysql
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
bad = blacklist.bad

def find(word):
	count = 0
	for txt in text:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				count = count + 1
	return count

list = {}
list2 = {}
def words():
	global list
	for txt in text:
		tx = open(txt, "r").readlines()
        
		for b in tx:
			for c in b.split():
				if ":" in c: c = c[:-1]
				if str(c) not in bad and c != "" and len(str(c)) > 3 or str(c) in blacklist.exception:
					if find(c) > 6:
						list.update({c:find(c)})
						list2.update({c:find(c)})


	list = OrderedDict(sorted(list.items(), key=lambda x:x[1]))
	
	print time.strftime("%H:%M %d.%m.%Y")
	print 
	
 	for l in reversed(list):
 		if list[l] > 6 and l not in bad:
 			print l + ": " + str(list[l])

def data():
	try:
		os.mkdir(dir)
	except OSError:
		pass
	most = open(dir + time.strftime("%Y.%m.%d") + ".data", "w+")

	for l in reversed(list):
		if list[l] > 6 and l not in bad and l != "":
			most.write(l + ": " + str(list[l]) + '\n')

	most.close()

def rawdata():
	schlagzeilen = open(dir + "news-" + time.strftime("%Y.%m.%d") + ".txt", "w+")

	for txt in text:
		for lines in open(txt, "r").readlines():
			schlagzeilen.write(lines[:-1] + " (" + txt[5:-4] + ")" + "\n")
	
	schlagzeilen.close()

words()
data()
rawdata()
mysql.main(list2)