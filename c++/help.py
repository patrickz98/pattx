import os
import sys

def clean():
	dir =  os.listdir(".")

	for x in dir:
		for y in dir:
			if x == y[:-4]:
				print "clean --> " + x
				os.remove(x)

def list():
	dir =  os.listdir(".")

	for x in dir:
			if ".cpp" in x:
				print "\tg++ " + x + " -o " + x[:-2]

def gcc(file):
	print "g++ " + file + " -o " + file[:-2]
	os.system("g++ " + file + " -o " + file[:-2])

if sys.argv[1] == "clean":
	clean()
elif sys.argv[1] == "list":
	list()
else:
	gcc(sys.argv[1])
#	print "NOOO"
