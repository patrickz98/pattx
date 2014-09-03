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
		
	file.close()


def main():
	files = os.popen("ls words").readlines()
	for txt in files:
		txt = txt[:-1]
		if ".data" in txt:
			clean("words/" + txt)

main()
