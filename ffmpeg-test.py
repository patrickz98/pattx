#!/usr/bin/python
import sys
import os
import time

print "hallo"

input = sys.argv
input.remove(input[0])

decoder =[]
for i in input:
	if i == "-o":
		print input[input.index(i) + 1]
		#input.remove(input[input.index(i) + 1])
		#input.remove(i)
		#count += 1
	elif i == "-i":
		print input[input.index(i) + 1]
		#input.remove(input[input.index(i) + 1])
		#input.remove(i)
		#count += 1

print input 
print decoder

"""
import signal
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print('Press Ctrl+C')
#signal.pause()
while(True):
	print "hallo"

name = "odroid@odroid.local"
print name.find("@")
print name[:name.find("@")]
print "format = " + name[name.find("@") + 1:]

h = "hhdf",\
	"jhasjdh",\
	"kj" 

print h


while(True):
	#i = time.clock()
	sys.stdout.write('\r %s ' % str(time.clock()))
	sys.stdout.flush() 
	#time.sleep(1)
"""
	

