import os
import sys

def clean():
	dir =  os.listdir(".")

	for x in dir:
		for y in dir:
			if x == y[:-2]:
				print "clean --> " + x
				os.remove(x)

def list():
	dir =  os.listdir(".")

	for x in dir:
			if ".c" in x:
				print "\tgcc " + x + " -o " + x[:-2]

if sys.argv[1] == "clean":
	clean()
elif sys.argv[1] == "list":
	list()
else:
	print "NOOO"