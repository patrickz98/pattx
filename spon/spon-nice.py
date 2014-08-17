#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

schlagzeilen = open("news-spon.txt", "w+")
os.popen("curl http://www.spiegel.de/schlagzeilen/ 1>spon.txt 2>/dev/null").readlines
txt = open("spon.txt", "r").readlines()

for a in txt:
	if "title=" in a:
		find = re.search("title=(.*?)>", a)
		
		if find.group(0) != 'title="Anzeige">':
#			print find.group(0)[7:-2]

			b = find.group(0)[7:-2]
		
			if "\\xfc" in b: b = re.sub(r"\\xfc", "ü", b)
		        if "\\xf6" in b: b = re.sub(r"\\xf6", "ö", b)
		        if "\\xdf" in b: b = re.sub(r"\\xdf", "ß", b)
		        if "\\xe4" in b: b = re.sub(r"\\xe4", "ä", b)

		        if "&quot;" in b: b = re.sub(r"&quot;", '"', b)
		        if "\\xa0" in b: b = re.sub(r"\\xa0", " ", b)
		        if "\\xd6" in b: b = re.sub(r"\\xd6", "Ö", b)
#		        if "\\xc3" in b: b = re.sub(r"\\xc3", "", b)

			
			schlagzeilen.write(b + "\n")


#txt.close()
schlagzeilen.close()

os.popen("python regex.py").readlines()
os.popen("rm spon.txt").readlines()
