#!/usr/bin/python
import os
import re
import regexhtml

def sueddeutsche():
	schlagzeilen = open("news-sueddeutsche.txt", "w+")
	os.popen("curl http://www.sueddeutsche.de/ 1>sueddeutsche.txt 2>/dev/null").readlines
	txt = open("sueddeutsche.txt", "r").read()

	find = re.findall(".*<strong>(.*?)</strong>.*?<em>(.*?)</em>.*", txt)
	find2 = re.findall(".*?<em>(.*?)</em>.*", txt)

	bla = []
	for a in find:
		schlagzeilen.write(str(a[0]) + ": " + str(a[1]) + "\n")
		bla.append(a[1])

	for b in find2:
		if b not in bla and len(b) > 15 and "SZ" not in b and "Bundesliga" not in b and "Kalender" not in b and "ueddeutsche" not in b:
			schlagzeilen.write(str(b) + "\n")

	schlagzeilen.close()
	os.popen("rm sueddeutsche.txt").readlines()
	regexhtml.main("news-sueddeutsche.txt")

