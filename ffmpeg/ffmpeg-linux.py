#!/usr/bin/python
import subprocess
import sys
import os
import time
import socket

hosts = ["patty@debian.local"]

#linux
wwwdirec = "/var/www/odroid/"
localhost = socket.gethostname() + ".local" #hostname

#OSX !sudo apachectl start
#wwwdirec = "/Library/WebServer/Documents/"
#localhost = socket.gethostname()
#localhost = socket.gethostbyname(socket.gethostname()) #ip

pwd = os.getcwd()
localhostuser = os.getlogin() #user


input = sys.argv
input.remove(input[0])

file = ""
ofile = ""

#function for analyze the imput -i and -o 
if "-i" in input and "-o" in input:
	for i in input:
		if i == "-i":
			file += input[input.index(i) + 1]
		elif i == "-o":
			ofile += input[input.index(i) + 1]
else:
	print "input error: please use ffmpeg-extern -i input-video -o endvideo.mp4"
	exit()

#name extraction
name = file[:file.find(".")]
formart = file[file.find("."):]
endname = ofile[:ofile.find(".")]
endformat = ofile[ofile.find("."):]

#video length
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
		exit()

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
	while (len(hosts) > a):
		c = seconds / len(hosts)
		b = b + c
		d = b - c
		print ("cut from %d to %d" % (d, b))
		
		out = endname + "-part-" + str(a)
		videoparts.update({out:[int(d),int(b)]})

		a = a + 1

#ssh command transfer
hostlist = {}
def sshmain():
	a = 0
	for h in hosts:
		part = endname + "-part-%s" % str(a)
		hostlist.update({h:part})
		ssh(h, part)
		a += 1
			
buildparts = []
def ssh(HOST, part):
	part1 = videoparts[part][0]
	part2 = videoparts[part][1]
	out = part + endformat
	buildparts.append(out)

	print HOST + " make part = " +  part
	
	COMMAND = "nohup /usr/local/bin/ffmpeg -i http://%s/%s -ss %d -t %d %s 1>/dev/null 2>/dev/null &&\
		   scp ~/%s %s@%s:%s 1>/dev/null 2>/dev/null &&\
		   ssh %s@%s touch %s/%s-done &&\
		   rm ~/%s &" \
		   % (localhost, file, part1, part2, out, 
		      out, localhostuser, localhost, pwd, 
		      localhostuser,localhost, pwd, out, 
		      out)
	
	subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)

#creat symlinks
def symlink(file):
	os.popen('rm %s%s' % (wwwdirec, file)).readlines()
	print "make symlink from %s to %s%s" % (file, wwwdirec, file)
	os.popen('ln -s %s/%s %s%s' % ( pwd, file, wwwdirec, file)).readlines()
	
#link the videos 
def linkVideos():
	finish = []
	while(True):
		objects = os.popen('ls').readlines()
		for a in objects:
			for b in buildparts:
				if a[:-1] == b + "-done":
					print a[:-1] + " is received"

					if finish:
						if b in finish:
							pass
						else:
							finish += [b]
					else:
						finish += [b]
					
		if (len(finish) == len(hosts)):
			print "build video..............."
			finish2 = []
			
			if endformat == ".mp4" or endformat == ".mov" or endformat == ".m4a":
				for a in finish:
					if "0" in a:
						finish2 += ["-add " + a]
					else:
						finish2 += ["-cat " + a]

				build = ' '.join(sorted(finish2))
				os.popen('MP4Box %s %s%s' % (build, endname, endformat)).readlines()
				break
			else:
				finish = ' '.join(sorted(finish))
				os.popen('mencoder -oac copy -ovc copy -idx -o %s%s %s' % (endname, endformat, finish)).readlines()
				break
		else:
			print "Wait of hosts - " + time.strftime("%H:%M:%S")
#			for a in hostlist:
#				for b in finish:
#					if hostlist[a] == b:
#						print "%s has finish" % a

			time.sleep(2)	

def clean():
	print "cleaning system....." 
	os.popen('rm %s%s' % (wwwdirec, file)).readlines()
	os.popen('rm %s-part-*%s' % (endname, endformat)).readlines()
	os.popen('rm %s-part-*%s-done' % (endname, endformat)).readlines()

def ping():
	print "ping all hosts in list"
	down = []
	for h in hosts:
		host = h[h.find("@") + 1:]
		#response = os.system("ping -c 1 " + host)
		response = subprocess.call("ping -c 1 %s" % host,
    			   shell=True,
    			   stdout=open('/dev/null', 'w'),
    			   stderr=subprocess.STDOUT)
		
		if response == 0:
			print host, 'is up!'
		else:
			print host, 'is down!'
			down.append(h)
		
	for x in down:hosts.remove(x)
		
	if len(hosts) == 0:
		print "no hosts online"
		exit()
"""*
#strg+c
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
"""
def main():
	ping()
	getvideoparts(file)
	symlink(file)
	sshmain()
	linkVideos()
	clean()

main()
