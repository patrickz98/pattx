#!/usr/bin/python
import os
import re

def tagesspiegel():
	schlagzeilen = open("news-tagesspiegel.txt", "w+")
	os.popen("curl http://www.tagesspiegel.de/schlagzeilen/ 1>tagesspiegel.txt 2>/dev/null").readlines
	txt = open("tagesspiegel.txt", "r").read()

	find = re.findall('<a title=\"(.*?)\"', txt)
	bla = []

	for i in find:
		if len(i) > 15 and i not in bla and "Tagesspiegel" not in i and "Mediadaten" not in i and "Sie haben Mut zur Uni" not in i:
			schlagzeilen.write(i + "\n")
			bla.append(i)

	schlagzeilen.close()
	os.popen("rm tagesspiegel.txt").readlines()

