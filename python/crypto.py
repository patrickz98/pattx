#!/usr/bin/python

import sys
import os


input = sys.argv
input.remove(input[0])

file = ""
ofile = ""

for i in input:
	if i == "-i":
		file += input[input.index(i) + 1]
	if i == "-o":
		ofile += input[input.index(i) + 1]

def encrypt():
	os.popen("openssl aes-256-cbc -a -salt -in %s -out %s.crypt" % ( file, file)).readlines()

def decrypt():
	os.popen("openssl aes-256-cbc -d -a -in %s -out %s" % ( ofile, (ofile[:-6]))).readlines()

if ofile == "":
	encrypt()
else:
	decrypt()
