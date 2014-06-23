#!/usr/bin/python

import subprocess
import sys
import os
from config import *

pwd = os.getcwd()
slaves = 2

#file = "../thrones-4x03-copy.ts"
#file = "test.ts"
#file = "../Recordings/Jerry-Cotton/Jerry-Cotton.mkv"
file = "see.ts"

#Video length
def getLength(file):
	result = subprocess.Popen(["ffprobe", file], 
		stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	length = str([x for x in result.stdout.readlines() if "Duration" in x])
	
	cut1 = length.find(": ") + 2
	cut2 = length.find(",")
	length = length[cut1:cut2]

	if  length:
		return length
	else:
		print "video error"
	
#Video cutter
videoparts = []
def cut(file):
	length = getLength(file)
	h = int(length[:2])
	m = length[3:(len(length) - 6)]
	s = length[6:]
	seconds = (int(h) * 60  + int(m)) * 60 + float(s)
	
	print "seconds in video: " + str(seconds)
	
	a = 0
	b = 0
	while (slaves > a):
		c = seconds / slaves
		b = b + c
		d = b - c
		print ("cut from %d to %d" % (d, b))
		a = a + 1
		
		out = "out-" + str(a) + ".ts"
		os.popen("ffmpeg -i %s -acodec copy -vcodec copy -scodec copy -ss %s -t %s %s 1>/dev/null 2>/dev/null" % (str(file), str(d), str(b), out)).readlines()
		
		videoparts.append(out)

#link the videos 
def build():
	bulid = "concat:"
	for i in videoparts:
		bulid += i + "|"
	os.popen('ffmpeg -i "%s" -vcodec copy -acodec copy  end.ts 1>/dev/null 2>/dev/null' % (bulid)).readlines()

#ssh command transfer
def sshhead():
	for h in hosts:
		ssh(h)

def ssh(HOST):
	#HOST = "odroid-u4.local"
	COMMAND = "ffmpeg -i http://odroid-u3.local/out-2.ts out.mp4; scp out.mp4 odroid@odroid-u3.local:%s; rm out.mp4" % pwd

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
	    error = ssh.stderr.readlines()
	    #print >>sys.stderr, "ERROR: %s" % error
	    return "ssh error" 
	else:
	    return  str(result)[2:-4]

#Creat symlinks
def symlinks():
	for i in videoparts:
		print "make symlink from %s to /var/www/odroid/%s" % ( i, i)
		os.popen('ln -s %s/%s /var/www/odroid/%s' % ( pwd, i, i)).readlines()
	


#print getLength(file)
#cut(file)
#symlinks()
sshhead()
#print "build"
#build()
