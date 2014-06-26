#!/usr/bin/python

import subprocess
import sys
import os
import time
from config import *

pwd = os.getcwd()
slaves = len(hosts)

#file = "thrones-4x04.ts"
#file = "test.ts"
#file = "../Recordings/Jerry-Cotton/Jerry-Cotton.mkv"

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
videoparts = {}
def getvideoparts(file):
	length = getLength(file)
	h = int(length[:2])
	m = length[3:(len(length) - 6)]
	s = length[6:]
	seconds = (int(h) * 60  + int(m)) * 60 + float(s)
	
	print "seconds in video: " + str(seconds)
	
	a = 0
	b = 0
	while (slaves >= a):
		c = seconds / slaves
		b = b + c
		d = b - c
		print ("cut from %d to %d" % (d, b))
		
		out = "part-" + str(a)
		#os.popen("ffmpeg -i %s -acodec copy -vcodec copy -scodec copy -ss %s -t %s %s 1>/dev/null 2>/dev/null" % (str(file), str(d), str(b), out)).readlines()
		#videoparts.append(out)
		videoparts.update({out:[int(d),int(b)]})
		print out
		print videoparts[out]
		a = a + 1

#ssh command transfer
def sshhead():
	a = 0
	for h in hosts:
		part = "part-%s" % str(a)
		#part = a
		ssh(h, part)
		a += 1

buildparts = []
def ssh(HOST, part):
	global buildparts
	#HOST = "odroid-u4.local"
	part1 = videoparts[part][0]
	part2 = videoparts[part][1]
	out = part + ".mp4"
	print "%s" % out
	buildparts.append(out)
	
	#main ssh 
	COMMAND = "nohup ffmpeg -i http://odroid-u3.local/%s -ss %d -t %d %s 1>/dev/null 2>/dev/null && scp ~/%s odroid@odroid-u3.local:%s 1>/dev/null 2>/dev/null && rm ~/%s" % (file, part1, part2, out, out, pwd, out)
	subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)

#Creat symlinks
def symlink(file):
	print "make symlink from %s to /var/www/odroid/%s" % (file, file)
	os.popen('rm /var/www/odroid/%s' % file).readlines()
	os.popen('ln -s %s/%s /var/www/odroid/%s' % ( pwd, file, file)).readlines()
	
#link the videos 
def build():
	bulid = "concat:"
	finish = []
	while(True):
		objects = os.popen('ls').readlines()
		for a in objects:
			for b in buildparts:
				if a[:-1] == b:
					print a[:-1] + " is finish"
					finish.append(a)
				
		print "len(finish) " + str(len(finish))
		print str(slaves)
		if (len(finish) == slaves):
			for i in finish:
				bulid += i + "|"
			os.popen('ffmpeg -i "%s" -vcodec copy -acodec copy end.mp4 1>/dev/null 2>/dev/null' % (bulid)).readlines()
			break
		else:
			print "Wait of hosts"
			time.sleep(15)
		
	
print getLength(file)
getvideoparts(file)
symlink(file)
sshhead()
print "build"
build()
