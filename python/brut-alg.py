#!/usr/bin/python

lst = "abcdefghijklmnopqrstuvwxyz"
print len(lst)

#my_list = [for i in lst]
my_file = open("output.txt", "a")

# Add your code below!
for i in lst:
    my_file.write(str(i) + "\n")
    print i,
    for l in lst:
	my_file.write(str(i) + str(l) + "\n")
	print i + l,
#	for u in lst:
#	    my_file.write(str(i) + str(l) + str(u) + "\n")
#	    print i + l + u
#	    for x in lst:
#            	my_file.write(str(i) + str(l) + str(u) + str(x) + "\n")
#		print i + l + u + x

my_file.close()
