#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import sys
from urllib2 import Request, urlopen, URLError

def download(url, file):
	request = Request(url + "/images/" + file)
	html = 0

	try:
		response = urlopen(request)
		html = response.read()
		sys.stdout.write("Download: " + file.replace("%20", "-") + "\n") 

	except URLError, e:
		sys.stdout.write('Error:', e)

	img = open(file.replace("%20", "-"), 'wb')
	img.write(html)
	img.close()

def get(url):
	ur_url = url.split("://")[1].split("/", 1)[0]

	request = Request(url)

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
		sys.stderr.write('Error:', e)

	find = re.findall("<img.*?src=\"(.*?)\".*?>", html)

	for x in find:
		if "images" in x:
			file = x.split("/")[len(x.split("/")) - 1].replace(" ", "%20").replace("1__", "")
			download("http://" + ur_url, file)

url = input('Enter URL: ')

get(url.replace("https", "http"))
