#!/usr/bin/python
import re
import os

def main(word, text):
	dataori = open(text, "r").readlines()
	
	besetzt = []
	data = []
	for z in dataori:
		if z not in data and not z == '\n' and z[:z.index(":")] == word:
			data.append(z)

	size = []
	for a in data:
		find = re.findall(".*: (.*?) date:", a)
		size.append(int(''.join(find)))

	name = data[0][:data[0].index(":")]

	print name
	sizesort = sorted(size)
	for b in reversed(range(1, int(sizesort[len(sizesort) - 1]) + 1)):
		line = []
		if b in size:
			find = [i for i in range(len(size)) if size[i] == b]
		else:
			find = False
		
		if len(str(b)) == 1:
			
			line.append("0" + str(b) + "|")

			if find != False:
				for posi in find:
					if " ! " in line:
						line.append("   " * 1)
						line.append(" ! ")
					else:
						line.append("   " * posi)
						line.append(" ! ")
#					besetzt.append(len(''.join(line)))
#					print "besetzt ", besetzt

		else:
			
			line.append(str(b) + "|")

			if find != False:			
				for posi in find:
					if " ! " in line:
						line.append("   " * 1)
						line.append(" ! ")
					else:
						line.append("   " * posi)
						line.append(" ! ")
#					besetzt.append(len(''.join(line)))
#					print "besetzt ", besetzt
					
		print ''.join(line)
	
	print "  +" + "---" * len(size) * 2
	numbers = "   "
	for number in range(1, len(size) * 2):
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

	for txt in data:
		line = txt[:txt.index(":")]
		if line == word and txt[:-1] not in nown:
			print txt[:-1]
			nown.append(txt[:-1])

os.popen("python data.py > data-raw.txt").readlines()
text = open("data-raw.txt", "r").readlines()
words = []
for line in text:
	if not line[:line.index(":")] in words:
		words.append(line[:line.index(":")])

for w in words:
	main(w, "data-raw.txt")
	