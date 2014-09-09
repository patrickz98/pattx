#!/usr/bin/python
import re
import time

import data

def graph(word, text):
	dataori = text	
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
		print "<h1>" + word + "</h1>"
		sizesort = sorted(size)
		lines = {}

		for b in range(1, int(sizesort[len(sizesort) - 1]) + 1):
			if len(str(b)) == 1:
				lines.update({b:"0" + str(b) + "|"})
			else:
				lines.update({b:str(b) + "|"})
	
		for c in size:
			lines.update({c:''.join(lines[c]) + "&nbsp;!&nbsp;"})
			for d in range(1, int(sizesort[len(sizesort) - 1]) + 1):
				if d != c:
					lines.update({d:''.join(lines[d]) + "&nbsp;&nbsp;&nbsp;"})
		
		for y in reversed(sorted(lines.keys())):
			print "<div>" + lines[y] + "</div>"

		print "<div>" + "&nbsp;&nbsp;+" + "---" * (len(size) + 4) + "</div>"
		numbers = "&nbsp;&nbsp;&nbsp;"
		for number in range(1, (len(size) + 4)):
			if len(str(number)) == 1:
				numbers += str("&nbsp;%d&nbsp;" % number)
			else:
				numbers += str("&nbsp;%d" % number)
			
		print "<div>" + numbers + "</div>"
		print "<div>" + "&nbsp;" + "</div>"
		date(word, text)

def date(word, text):
	data = text
	nown = []
	count = 1

	for txt in data:
		line = txt[:txt.index(":")]
		if line == word and txt not in nown:
			print "<div>" + str(count) + "&nbsp;:&nbsp;" + txt + "</div>"
			nown.append(txt)
			count = count + 1

def main():
	text = data.main()
	words = []

	print "<!DOCTYPE html>"
	print "<html>"
	print "<div>" + time.strftime("%H:%M %d.%m.%Y") + "</div>"

	for line in text:
		if not line[:line.index(":")] in words:
			words.append(line[:line.index(":")])

	for w in words:
		graph(w, text)
	print "</html>"
main()