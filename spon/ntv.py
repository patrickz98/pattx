#!/usr/bin/python
import os
import re

def ntv():
	schlagzeilen = open("news-ntv.txt", "w+")
	os.popen("curl http://www.n-tv.de/ 1>ntv.txt 2>/dev/null").readlines
	txt = open("ntv.txt", "r").readlines()

	safe = ""
	for a in txt:
		if "<span class=\"" in a and "</span>" in a:
			find = re.search('<span class=.*?>(.*?)</span>', a)
			schlagzeilen.write(find.group(1) + "\n")


	schlagzeilen.close()
	os.popen("rm ntv.txt").readlines()
	os.popen("python regex-ntv.py").readlines()
