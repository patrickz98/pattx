#!/usr/bin/python
import re
import os
import time

def graph(word, text):
	dataori = open(text, "r").readlines()
	
	count = 0
	data = []
	for z in dataori:
		if z not in data and not z == '\n' and z[:z.index(":")] == word:
			data.append(z)

	size = []
	for a in data:
		find = re.findall(".*: (.*?) date:", a)
		size.append(int(''.join(find)))

	if len(size) >= 2:
		print word
		sizesort = sorted(size)
		lines = {}

		for b in range(1, int(sizesort[len(sizesort) - 1]) + 1):
			if len(str(b)) == 1:
				lines.update({b:"0" + str(b) + "|"})
			else:
				lines.update({b:str(b) + "|"})
	
		for c in size:
			lines.update({c:''.join(lines[c]) + " ! "})
			for d in range(1, int(sizesort[len(sizesort) - 1]) + 1):
				if d != c:
					lines.update({d:''.join(lines[d]) + "   "})
		
		for y in reversed(sorted(lines.keys())):
			print lines[y]

		print "  +" + "---" * (len(size) + 4)
		numbers = "   "
		for number in range(1, (len(size) + 4)):
			if len(str(number)) == 1:
				numbers += str(" %d " % number)
			else:
				numbers += str(" %d" % number)
			
		print numbers
		print
		date(word, "data-raw.txt")
		print

def date(word, text):
	data = open(text, "r").readlines()
	nown = []
	count = 1

	for txt in data:
		line = txt[:txt.index(":")]
		if line == word and txt[:-1] not in nown:
			print str(count) + ": " + txt[:-1]
			nown.append(txt[:-1])
			count = count + 1

def main():
	os.popen("python data.py > data-raw.txt").readlines()
	text = open("data-raw.txt", "r").readlines()
	words = []

	print time.strftime("%H:%M %d.%m.%Y")
	print 

	for line in text:
		if not line[:line.index(":")] in words:
			words.append(line[:line.index(":")])

	for w in words:
		graph(w, "data-raw.txt")
main()