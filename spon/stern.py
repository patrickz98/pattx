#!/usr/bin/python
import os
import re

schlagzeilen = open("news-stern.txt", "w+")
os.popen("curl http://www.stern.de/news/ 1>stern.txt 2>/dev/null").readlines
txt = open("stern.txt", "r").readlines()

for a in txt:
	if '<span class="head">' in a:
		find = re.search('<span class="head">(.*?)</span>', a)
		schlagzeilen.write(find.group(1) + "\n")


schlagzeilen.close()
os.popen("rm stern.txt").readlines()
