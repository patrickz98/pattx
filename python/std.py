import sys
#import time

sys.stdout.write("OUT\n")
sys.stderr.write("ERR\n")

for x in range(0, 100000):
	sys.stdout.write(str(x) + "\r")
	sys.stdout.flush()
#	time.sleep(1)

sys.stdout.write("\n")

