#!/usr/bin/python
import os
import re

schlagzeilen = open("news-welt.txt", "w+")
os.popen("curl http://www.welt.de/ 1>welt.txt 2>/dev/null").readlines
txt = open("welt.txt", "r").readlines()

for a in txt:
	if "<h4>" in a and "<span>" in a:
		find = re.search("<span>(.*?)</span>(.*?)</a>", a)
		schlagzeilen.write(find.group(1) + " " + find.group(2) + "\n")


schlagzeilen.close()
os.popen("rm welt.txt").readlines()
