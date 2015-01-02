#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
from urllib2 import Request, urlopen, URLError

def download(url):
	request = Request(url)
	html = 0

	try:
		response = urlopen(request)
		html = response.read()
		sys.stdout.write("Download: " + url.split("/")[len(url.split("/")) - 1].replace("%20", "-") + "\n") 
	except URLError, e:
		print 'Error:', e

	img = open(url.split("/")[len(url.split("/")) - 1].replace("%20", "-"), 'wb')
	img.write(html)
	img.close()

def get(url, count):
	ur_url = url.split("://")[1].split("/", 1)[0]

	for n in range(0, count):
		request = Request(url + str(n))

		try:
			response = urlopen(request)
			html = response.read()
		except URLError, e:
			sys.stderr.write('Error:', e)

		find = re.findall("<img.*?src=\"(.*?)\".*?>", html)
		download("http://" + ur_url + find[0].replace(" ", "%20").replace("1__", ""))

url = input('Enter URL: ')
size = input('Enter pictures size: ')

get(url.replace("https", "http"), size - 1)
