#!/usr/bin/python
import subprocess
import sys
import os
import time

pwd = os.getcwd()
hosts = ["odroid@odroid-u4.local", "patty@debian.local", "odroid@odroid-x2.local"]
slaves = len(hosts)
localhost = "odroid-u3.local"
localhostuser = "odroid"
wwwdirec = "/var/www/odroid/"

#file = "thrones-4x04.ts"
#file = "test.ts"
#file = "loriot.mp4"
file = "see.ts"

name = file[:file.find(".")]
formart = file[file.find("."):]
endname = "see"
endformat = ".mp4"

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
		
		out = endname + "-part-" + str(a)
		videoparts.update({out:[int(d),int(b)]})
		#print out
		#print videoparts[out]
		a = a + 1

hostlist = {}
#ssh command transfer
def sshmain():
	a = 0
	for h in hosts:
		if ping(h) == 0:
			part = endname + "-part-%s" % str(a)
			print "host " + h + " calculating " + part
			hostlist.update({h:part})
			ssh(h, part)
			a += 1
		elif ping(h) == 1:
			print "host %s is not available" % h
			hosts.remove(h)
			
buildparts = []
def ssh(HOST, part):
	part1 = videoparts[part][0]
	part2 = videoparts[part][1]
	out = part + endformat
	buildparts.append(out)
	
	COMMAND = "nohup ffmpeg -i http://%s/%s -ss %d -t %d %s 1>/dev/null 2>/dev/null &&\
		scp ~/%s %s@%s:%s 1>/dev/null 2>/dev/null &&\
		ssh %s@%s touch %s/%s-done &&\
		rm ~/%s"\
		% (localhost, file, part1, part2, out, 
		   out, localhostuser, localhost, pwd, 
		   localhostuser,localhost, pwd, out, 
		   out)
	
	subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)

#Creat symlinks
def symlink(file):
	os.popen('rm %s%s' % (wwwdirec, file)).readlines()
	print "make symlink from %s to %s%s" % (file, wwwdirec, file)
	os.popen('ln -s %s/%s %s%s' % ( pwd, file, wwwdirec, file)).readlines()
	
#link the videos 
def make():
	finish = []
	while(True):
		objects = os.popen('ls').readlines()
		for a in objects:
			for b in buildparts:
				if a[:-1] == b + "-done":
					print a[:-1] + " is received"
					
					if finish:
						if b in finish:
							print "%s is in finish" % b
						else:
							print "add %s to finish" % b
							finish += [b]
					else:
						finish += [b]
						
		if (len(finish) == slaves):
			build = ' '.join(finish)
			#os.popen('ffmpeg -i "%s" -vcodec copy -acodec copy %s%s 1>/dev/null 2>/dev/null' % (bulid, endname, endformat)).readlines()
			os.popen('mencoder -oac pcm -ovc copy -o %s%s %s 1>/dev/null 2>/dev/null' % (endname, endformat, build)).readlines()
			break
		else:
			print "Wait of hosts - " + time.strftime("%H:%M:%S")
			
			for a in hostlist:
				for b in finish:
					if hostlist[a] == b:
						print "%s has finish" % a
					else:
						print "wait of %s" % a
			
			time.sleep(15)	

def clean():
	print "cleaning system....." 
	os.popen('rm %s%s' % (wwwdirec, file)).readlines()
	os.popen('rm %s-part-*%s' % (endname, endformat)).readlines()
	os.popen('rm %s-part-*%s-done' % (endname, endformat)).readlines()

def ping(h):
	host = h[h.find("@") + 1:]
	#response = os.system("ping -c 1 " + host)
	response = subprocess.call("ping -c 1 %s" % host,
        shell=True,
        stdout=open('/dev/null', 'w'),
        stderr=subprocess.STDOUT)
	
	if response == 0:
		#print host, 'is up!'
		return 0
	else:
		#print host, 'is down!'
		return 1

def main():
	print getLength(file)
	getvideoparts(file)
	symlink(file)
	sshmain()
	make()
	#clean()

main()
