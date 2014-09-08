#!/usr/bin/python
import os
import blacklist

def clean(txt):
	news2 = open(txt, "r")
	news = news2.readlines()
	news2.close()
	file = open(txt, "w+")
	
	for w in news:
		b = w[:w.index(":")]
		bad = blacklist.bad
		if b not in bad:
			file.write(w)
		else:
			print "clean:", b, "in", txt
	file.close()


def main():
	dir = "./words/"
	files = os.listdir(dir)
	for txt in files:
		if ".data" in txt:
			clean(dir + txt)

main()
