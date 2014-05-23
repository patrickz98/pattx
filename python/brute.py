import mechanize
import cookielib

my_file = open("out-r.txt", "r+")
my_file1 = my_file.readlines()
passwords = open("passwords.txt", "a")
user = 'patrick.zierahn'
passwd = 'blabla123'

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
	#return len(b)

"""
print check(user, passwd)
print len(my_file1) - 1
"""
if check(user, passwd) == len(my_file1) - 1:
	print "Juhuu"
	#passwords.write(str(user) + "\n")
	#passwords.write(str(passwd) + "\n")
else:
	print "Oh"

my_file.close()
passwords.close()
