#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import time

request = urllib2.Request('http://finance.yahoo.com/d/quotes.csv?s=AAPL&f=n+o+p2+p5')
	
try:
	response = urllib2.urlopen(request)
	html = response.read()
except urllib2.URLError, e:
    print 'Error:', e

print html

request = urllib2.Request('http://quote.yahoo.com/d/quotes.csv?s=JPYUSD=X&f=nl1d1t1')

try:
    response = urllib2.urlopen(request)
    html = response.read()
except urllib2.URLError, e:
    print 'Error:', e

print html
