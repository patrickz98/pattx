#!/usr/bin/python
import os
import re

def faz():
	schlagzeilen = open("news-faz.txt", "w+")
	os.popen("curl http://www.faz.net/ 1>faz.txt 2>/dev/null").readlines
	txt = open("faz.txt", "r").readlines()

	for a in txt:
		if '<a title=' in a:
			find = re.search('<a title=\"(.*?)\"', a)
			if len(find.group(1)) > 15 and not "FAZ.NET-Comic-Roman" in find.group(1):
				schlagzeilen.write(find.group(1) + "\n")


	schlagzeilen.close()
	os.popen("rm faz.txt").readlines()
