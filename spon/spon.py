#!/usr/bin/python
import os

schlagzeilen = open("news-spon.txt", "w+")
os.popen("curl http://www.spiegel.de/schlagzeilen/ 1>spon.txt 2>/dev/null").readlines
txt = open("spon.txt", "r")

raw = str([x for x in txt.readlines() if "title=" in x])

tit = raw
title = []

while(True):
	if tit.find('title=') and not tit.find('title=') == -1:
		part1 = tit.find('title=') + 7
		part2 = tit.find('>')
	        t = str(tit[part1:part2 - 1])

		title.append(str(tit[part1:part2 - 1]))
		tit = tit[part2 + 1:]
	else:
		break

write = []
for t in title:
	if len(t) >= 8 and not 'Anzeige' in t and not 'nav-channel-name' in t and not 'SPIEGEL ONLINE' in t:
#		print t
		schlagzeilen.write(t + "\n")
		write.append(t)
	else:
#		print "remove"
		title.remove(t)

#z = b.split()

txt.close()
os.popen("rm spon.txt").readlines()
schlagzeilen.close()
os.popen("python regex.py").readlines()
