#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

os.popen("python spon.py").readlines()
os.popen("python zeit.py").readlines()
os.popen("python welt.py").readlines()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt"]
for txt in text:
	tx = open(txt, "r").readlines()
	for a in tx:
		if "US" in a:
			print a[:-1]
	
