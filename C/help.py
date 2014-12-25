import os

dir =  os.listdir(".")
data = {}

for x in dir:
	for y in dir:
		if x == y[:-2]:
			print "clean --> " + x
			os.remove(x)
