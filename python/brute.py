#!/usr/bin/python

import mechanize
import cookielib


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
br.form['login_act'] = 'patrick.zierahn'
br.form['login_pwd'] = 'blabla123'

# Login
a = br.submit()
b = a.read()

#r= br.open('https://goethe-schule-harburg.de/idesk/infodisplay/index.php?id=5')
#html = r.read()

print b
