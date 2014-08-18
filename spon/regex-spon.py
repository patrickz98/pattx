#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import fileinput

news2 = open("news-spon.txt", "r")
news = news2.readlines()
news2.close()

file = open("news-spon.txt", "w+")

bla = []
for w in news:
	b = w
	if "\\xfc" in b: b = re.sub(r"\\xfc", "ü", b)
	if "\\xf6" in b: b = re.sub(r"\\xf6", "ö", b)
	if "\\xdf" in b: b = re.sub(r"\\xdf", "ß", b)
	if "\\xe4" in b: b = re.sub(r"\\xe4", "ä", b)

	if "&quot;" in b: b = re.sub(r"&quot;", '"', b)
	if "\\xa0" in b: b = re.sub(r"\\xa0", " ", b)
	if "\\xd6" in b: b = re.sub(r"\\xd6", "Ö", b)
	if "\\xdc" in b: b = re.sub(r"\\xdc", "Ü", b)
	
	bla.append(b)
	file.write(b)


file.close()
