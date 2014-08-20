#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import encodings

def main(text):
	news2 = open(text, "r")
	news = news2.readlines()
	news2.close()
	file = open(text, "w+")


	bla = []
	for w in news:
		b = w
		if "&Auml;" in b: b = re.sub(r"&Auml;", "Ae", b)
		if "&auml;" in b: b = re.sub(r"&auml;", "ae", b)
		if "&Ouml;" in b: b = re.sub(r"&Ouml;", "Oe", b)
		if "&ouml;" in b: b = re.sub(r"&ouml;", "oe", b)

		if "&Uuml;" in b: b = re.sub(r"&Uuml;", "Ue", b)
		if "&uuml;" in b: b = re.sub(r"&uuml;", "ue", b)
		if "&szlig;" in b: b = re.sub(r"&szlig;", "ß", b)

		if "&quot;" in b: b = re.sub(r"&quot;", '"', b)


		if b not in bla:
			bla.append(b)
			file.write(b)


	file.close()
