#!/usr/bin/python
import re

def main(word, text):
	dataori = open(text, "r").readlines()

#	words = []
#	for word in dataori:
#		word = word[:word.index(":")]
#		if word not in words: 
#			words.append(word)
		
#	print words
	
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
					line.append("   " * posi)
					line.append(" ! ")
			
		else:
			
			line.append(str(b) + "|")

			if find != False:			
				for posi in find:
					line.append("   " * posi)
					line.append(" ! ")
		
		print ''.join(line)
	
	print "  +" + "---" * len(size) * 3
	numbers = "   "
	for number in range(1, len(size) * 3):
		if len(str(number)) == 1:
			numbers += str(" %d " % number)
		else:
			numbers += str(" %d" % number)
			
	print numbers

text = open("xxx.txt", "r").readlines()
words = []
for line in text:
	if not line[:line.index(":")] in words:
		words.append(line[:line.index(":")])

for w in words:
	main(w, "xxx.txt")
