#!/usr/bin/python
import os
import re

def zeit():
	schlagzeilen = open("news-zeit.txt", "w+")
	os.popen("curl http://www.zeit.de/news/index 1>zeit.txt 2>/dev/null").readlines
	txt = open("zeit.txt", "r").readlines()

	last = ""
	for a in txt:
		if "<span>" in a and "<strong>" in a:
			find = re.search("<strong>(.*?)</strong> <span>(.*?)</span>", a)
#			print find.group(1)[6:-7]
			if last != find.group(1) + ": " + find.group(2) + "\n":
				schlagzeilen.write(find.group(1) + ": " + find.group(2) + "\n")
				last = find.group(1) + ": " + find.group(2) + "\n"

	#txt.close()
	schlagzeilen.close()

	os.popen("rm zeit.txt").readlines()
