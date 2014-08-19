#!/usr/bin/python
import os
import re

def sueddeutsche():
	schlagzeilen = open("news-sueddeutsche.txt", "w+")
	os.popen("curl http://www.sueddeutsche.de/ 1>sueddeutsche.txt 2>/dev/null").readlines
	txt = open("sueddeutsche.txt", "r").read()

	find = re.findall("<strong>(.*?)</strong>.*?<em>(.*?)</em>", txt)

	for a in find:
		schlagzeilen.write(str(a) + "\n")

	#txt.close()
	schlagzeilen.close()

#	os.popen("rm sueddeutsche.txt").readlines()

sueddeutsche()
