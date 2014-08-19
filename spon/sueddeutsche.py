#!/usr/bin/python
import os
import re

def sueddeutsche():
	schlagzeilen = open("news-sueddeutsche.txt", "w+")
	os.popen("curl http://www.sueddeutsche.de/ 1>sueddeutsche.txt 2>/dev/null").readlines
	txt = open("sueddeutsche.txt", "r").readlines()

	last = ""
	for a in txt:
		if "<em>" in a and "</em>" in a:
			find = re.search("<em>(.*?)</em>", a)
#			print find.group(1)[6:-7]
			if last != find.group(1):
				schlagzeilen.write(find.group(1) + "\n")
				last = find.group(1) + "\n"

	#txt.close()
	schlagzeilen.close()

	os.popen("rm sueddeutsche.txt").readlines()

sueddeutsche()
