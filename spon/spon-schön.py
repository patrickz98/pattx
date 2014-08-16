#!/usr/bin/python
import os
import re

schlagzeilen = open("news-spon.txt", "w+")
os.popen("curl http://www.spiegel.de/schlagzeilen/ 1>spon.txt 2>/dev/null").readlines
txt = open("spon.txt", "r").readlines()

for a in txt:
	if "title=" in a:
		find = re.search("title=(.*?)>", a)
		
		if find.group(0) != 'title="Anzeige">':
			print find.group(0)[7:-2]
			schlagzeilen.write(find.group(1)[7:-2] + "\n")


#txt.close()
schlagzeilen.close()

os.popen("python regex.py").readlines()
os.popen("rm spon.txt").readlines()
