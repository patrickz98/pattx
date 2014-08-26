#!/usr/bin/python
import re

def main():
	dataori = open("data-sampel.txt", "r").readlines()
#	data = list(set(dataori))
	data = []
	for z in dataori:
		if z not in data:
			data.append(z)
	size = []

	for a in data:
		find = re.findall(".*: (.*?) date:", a)
		size.append(int(''.join(find)))

	sizesort = sorted(size)
	
	print sizesort
	print "sise", size
	
	for b in reversed(range(1, sizesort[len(sizesort) - 1] + 1)):
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
	
	print "  +" + "---" * len(size) * 2

main()
