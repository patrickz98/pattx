#!/usr/bin/python
import os
import re

schlagzeilen = open("news-zeit.txt", "w+")
os.popen("curl http://www.zeit.de/news/index 1>zeit.txt 2>/dev/null").readlines
txt = open("zeit.txt", "r").readlines()

title = []
for a in txt:
	if "<span>" in a and "<strong>" in a:
		find = re.search("<strong>(.*?)</strong> <span>(.*?)</span>", a)
#		print find.group(1)[6:-7]

		schlagzeilen.write(find.group(1) + ": " + find.group(2) + "\n")

#		find2 = re.search("<strong>(.*?)</strong> <span>", a)
#		print find2.group(0)[8:-16]

#txt.close()
schlagzeilen.close()

#os.popen("python regex.py").readlines()
os.popen("rm zeit.txt").readlines()
