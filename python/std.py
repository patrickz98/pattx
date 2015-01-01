import sys
#import time

sys.stdout.write("OUT\n")
sys.stderr.write("ERR\n")

for x in range(0, 100000):
	sys.stdout.write(str(x) + "\r")
	sys.stdout.flush()
#	time.sleep(1)

sys.stdout.write("\n")

def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in xrange(8):
        for fg in xrange(30,38):
            s1 = ''
            for bg in xrange(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print s1
        print '\n'

print_format_table()
