#!/usr/bin/python
import os

dir = "./words"
files = os.popen("ls %s/*" % dir).readlines()

a = "./words/20.08.2014-12.01.09.data"
file = open(a, "r")

for b in file:
	name = b[:b.find(":")]
	zahl = b[b.find(":") + 2:-1]

	files = ["./words/2014.21.08-17.53.22.data"]
	for c in files:
		c = c
		findf = open(c, "r").readlines()
		lasttyp = name
		lastzahl = zahl

		for d in findf:
			typ2 = d[:d.find(":")]
			zahl2 = d[d.find(":") + 2:-1]

			if name == typ2 and zahl2 > lastzahl:

				print b[:-1] + " date: " + a[8:-5]
				print d[:-1] + " date: " + c[8:-5]

			elif name == typ2 and zahl2 < lastzahl:

				print b[:-1] + " date: " + a[8:-5]
				print d[:-1] + " date: " + c[8:-5]
