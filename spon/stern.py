#!/usr/bin/python
import os
import re
import regexhtml

def stern():
	schlagzeilen = open("news-stern.txt", "w+")
	os.popen("curl http://www.stern.de/news/ 1>stern.txt 2>/dev/null").readlines
	txt = open("stern.txt", "r").readlines()

	last = ""	
	for a in txt:
		if 'title=\"' in a and '<a href=' in a:
			find = re.search('title=\"(.*?)\">', a)
			if len(find.group(1)) > 18 and len(find.group(1)) < 110:
				if last != find.group(1):
					schlagzeilen.write(find.group(1) + "\n")
					last = find.group(1)
					
	schlagzeilen.close()
	os.popen("rm stern.txt").readlines()
	regexhtml.main("news-stern.txt")
