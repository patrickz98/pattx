import os
import sys

input = sys.argv
input.remove(input[0])

if "-i" in input and "-o" in input:
	for i in input:
		if i == "-i":
			data_in = input[input.index(i) + 1]
		elif i == "-o":
			data_out = input[input.index(i) + 1]
else:
	print "input error:"
	exit()

for file in os.listdir("./"):
	if file.endswith(data_in):
		os.popen("ffmpeg -i " + file + " " + file[:-len(data_in)] + data_out)

