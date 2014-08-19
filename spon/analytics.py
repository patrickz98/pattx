
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
from collections import OrderedDict

import regex
import blacklist
import spon, zeit, welt, stern, faz, ntv


spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
ntv.ntv()
regex.main()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", "news-stern.txt"]

#most = open("woerter-der-woche.txt", "w+")

def find(word):
	count = 0
	for txt in text:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				count = count + 1
	return count



def words():
	list = {}
	bad = blacklist.bad
	for txt in text:
		tx = open(txt, "r").readlines()
        
		for b in tx:
			b = b
			for c in b.split():
				if str(c) not in bad:
					if find(c) >= 2:
						if ":" in c: c = c[:-1]
						list.update({c:find(c)})

#	list = OrderedDict(sorted(list.items(), key=lambda x:x[1]))
	for l in list:
		if list[l] > 6 and l not in bad:
			print l + ": " + str(list[l])
#			most.write(l + ": " + str(list[l]) + "\n")
words()
