#!/usr/bin/python
import os
import re


def spon():
	schlagzeilen = open("xxx.txt", "w+")
	os.popen("curl http://www.spiegel.de/schlagzeilen/ 1>spon.txt 2>/dev/null").readlines
	txt = open("spon.txt", "r").readlines()

	for a in txt:
		if "title=" in a:
#			a = re.comile()
			find = re.search('title=\"(.*?)\"', a, re.UNICODE)
#			if re.search("\S", find.group(1)) is not None: print find.group(1)
			schlagzeilen.write(find.group(1) + "\n")


	schlagzeilen.close()
#	os.popen("rm welt.txt").readlines()

spon()
