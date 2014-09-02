
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import time
from collections import OrderedDict

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

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", 
	    "news-stern.txt", "news-faz.txt", "news-ntv.txt", 
	    "news-tagesspiegel.txt", "news-sueddeutsche.txt"]


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


	list = OrderedDict(sorted(list.items(), key=lambda x:x[1]))
	for l in list:
		if list[l] > 6 and l not in bad:
			print l + ": " + str(list[l])
			result.append(l + ": " + str(list[l]))

def list():
	os.popen("mkdir -p words").readlines()

#	most = open("./words/" + time.strftime("%Y.%m.%d-%H.%M.%S") + ".data", "w+")
	most = open("./words/" + time.strftime("%Y.%m.%d") + ".data", "w+")

	for a in result:
		most.write(a + "\n")

print time.strftime("%H:%M %d.%m.%Y")
print 
words()
list()
