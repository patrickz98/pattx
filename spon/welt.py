#!/usr/bin/python
import os

schlagzeilen = open("welt-news.txt", "w+")
os.popen("curl http://www.welt.de/ 1>welt.txt 2>/dev/null").readlines
txt = open("welt.txt", "r")

raw = str([x for x in txt.readlines() if "name=" in x])

tit = raw
title = []

while(True):
	if tit.find('name=') and not tit.find('name=') == -1:
		part1 = tit.find('name=') + 7
		part2 = tit.find('>')
	        t = str(tit[part1:part2 - 1])

		title.append(str(tit[part1:part2 - 1]))
		tit = tit[part2 + 1:]
	else:
		break

write = []
for t in title:
	if len(t) >= 8 and not 'Anzeige' in t and not 'nav-channel-name' in t and not 'SPIEGEL ONLINE' in t:
		print t
#		schlagzeilen.write(t + '\n')
#		write.append(t)
#	else:
#		print "remove"
#		title.remove(t)

#z = b.split()

#x = []
#for a in write:
#	for b in write:
#		z = a.split()
#		y = b.split()
#		for c in z:
#			for d in y:
#				if c == d:
#					x.append(c)

#no = ["ein","von","zum","Das","Newsblog:","DerMorgen","@SPIEGELONLINE","in","im","stellt","sich","ist","der"]
#for v in x:
#	if v in no:
#		pass
#	else:
#		if v == "Obama":print v


txt.close()
schlagzeilen.close()
