#!/usr/bin/python
import os

def main():
	dir = "./words"
	files = sorted(os.popen("ls %s/*" % dir).readlines())
	nown = []
	raw = []
	for a in files:
		if ".data" in a:
			a = a[:-1]
			file = open(a, "r")

			for b in file:
				name = b[:b.find(":")]
				zahl = b[b.find(":") + 2:-1]

				if name not in nown:

					for c in files:
						c = c[:-1]
						findf = open(c, "r").readlines()
						lastzahl = zahl

						for d in findf:
							name2 = d[:d.find(":")]
							zahl2 = d[d.find(":") + 2:-1]

							if name == name2:

#								print b[:-1] + " date: " + a[8:-5]
#								print d[:-1] + " date: " + c[8:-5]
								raw.append(b[:-1] + " date: " + a[8:-5])
								raw.append(d[:-1] + " date: " + c[8:-5])


			nown.append(name)
			return raw