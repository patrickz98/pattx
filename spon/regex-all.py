#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import fileinput
import os

def main(txt):
	news2 = open(txt, "r")
	news = news2.readlines()
	news2.close()

	file = open(txt, "w+")

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
		if "\\xc4" in b: b = re.sub(r"\\xc4", "Ä", b)
		if "&amp;" in b: b = re.sub(r"&amp;", "&", b)

		if "\\xe9" in b: b = re.sub(r"\\xe9", "e", b)
		if "\\xf3" in b: b = re.sub(r"\\xf3", "o", b)
		if "\\xe7" in b: b = re.sub(r"\\xe7", "c", b)
		if "\\" in b: b = re.sub(r"\\", "'", b)
		
		if "Ä" in b: b = re.sub(r"Ä", "Ae", b)
		if "ä" in b: b = re.sub(r"ä", "ae", b)
		if "Ö" in b: b = re.sub(r"Ö", "Oe", b)
		if "ö" in b: b = re.sub(r"ö", "oe", b)
		if "Ü" in b: b = re.sub(r"Ü", "Ue", b)
		if "ü" in b: b = re.sub(r"ü", "ue", b)
		if "ß" in b: b = re.sub(r"ß", "ss", b)
		if "\"" in b: b = re.sub(r"\"", "", b)
		if "'" in b: b = re.sub(r"'", "", b)
		if "„" in b: b = re.sub(r"„", "", b)
		if "“" in b: b = re.sub(r"“", "", b)

		file.write(b)


	file.close()

files = os.listdir("./words/")
for txt in files:
	txt = "./words/" + txt
	if "news-" in txt:
		main(txt)