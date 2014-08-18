#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import encodings
import os

def uni(txt):
	news2 = open(txt, "r")
	news = news2.readlines()
	news2.close()

	file = open(txt, "w+")

	for w in news:
		b = w
		if "Ä" in b: b = re.sub(r"Ä", "Ae", b)
		if "ä" in b: b = re.sub(r"ä", "ae", b)
		if "Ö" in b: b = re.sub(r"Ö", "Oe", b)
		if "ö" in b: b = re.sub(r"ö", "oe", b)
		if "Ü" in b: b = re.sub(r"Ü", "Ue", b)
		if "ü" in b: b = re.sub(r"ü", "ue", b)

		file.write(b)
#		file.close()

def main():
	files = os.popen("ls").readlines()
	for txt in files:
		txt = txt[:-1]
		if "news-" in txt:
			uni(txt)

