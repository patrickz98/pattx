import subprocess
import sys

slaves = 2
file = "../thrones-4x03-copy.ts"
#file = "test.ts"

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
def cut(file):
	length = getLength(file)
	h = int(length[:2]) * 60
	m = length[3:(len(length) - 6)]
	s = length[6:]
	print int(h) / slaves
	print int(m) / slaves
	print float(s) / slaves

#	ffmpeg -i test.ts -acodec copy -vcodec copy -scodec copy -ss 00:00:00 -t 00:10:23.06 cut.ts	

#ssh command transfer
def ssh(COMMAND):
	HOST="odroid-u4.local"
	#COMMAND="uname -a"

	ssh = subprocess.Popen(["ssh", "%s" % HOST, COMMAND],
	                       shell=False,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
	    error = ssh.stderr.readlines()
	    print >>sys.stderr, "ERROR: %s" % error
	    return "ssh error" 
	else:
	    return  str(result)[2:-4]


#print ssh("uname -a")
#print ssh("uptime")
#print ssh("uptime")
print getLength(file)
cut(file)
