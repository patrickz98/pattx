#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import encodings

def main():
	news2 = open("news-ntv.txt", "r")
	news = news2.readlines()
	news2.close()

	file = open("news-ntv.txt", "w+")
	bla = []

	for w in news:
		b = w
		if re.search(r"^..:.*$", b) is not None or re.search(r"^[1-9].$", b) is not None or "<span class=" in b or "<img" in b or re.search(r"^10.$", b) is not None or re.search(r"^[0-9][0-9].[0-9].*$", b) is not None:
			bla.append(b)

		if b not in bla:
			bla.append(b)
			file.write(b)


	file.close()

