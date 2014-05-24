my_file1 = open("output.txt", "r+")
my_file2 = open("out-r.txt", "r+")
a = my_file1.readlines()
b = my_file2.readlines()

if a[4] != b[4]:
	print "ah"
else:
	print "oh"

my_file1.close()
my_file2.close()
