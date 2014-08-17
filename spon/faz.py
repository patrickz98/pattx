#!/usr/bin/python
import os
import re

schlagzeilen = open("news-faz.txt", "w+")
os.popen("curl http://www.faz.net/ 1>faz.txt 2>/dev/null").readlines
txt = open("faz.txt", "r").readlines()

for a in txt:
	if '<a title=' in a:
		find = re.search('<a title=\"(.*?)\"', a)
		schlagzeilen.write(find.group(1) + "\n")


schlagzeilen.close()
os.popen("rm faz.txt").readlines()
