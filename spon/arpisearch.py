#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

import conf
import arpigrapher
import regex
import spon, zeit, welt, stern, faz, ntv, tagesspiegel, sueddeutsche


spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
ntv.ntv()
tagesspiegel.tagesspiegel()
#sueddeutsche.sueddeutsche()
regex.main()

dir = conf.dir 
text = conf.text
htmldir = conf.htmldir

def count(word):
        count = 0
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                                count = count + 1
        return count


def title(word, html):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               html.write("<p>" +  a[:-1] + (" (%s)" % txt[5:-4]) + "</p>\n")

def archiv(word, html):
	archiv = sorted(os.listdir(dir))
	archiv = [conf.dir + x for x in archiv if "news-" in x]
	for txt in archiv:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				html.write("<p>" +  a[:-1] + (" (%s)" % txt[13:-4]) + "</p>\n")

def main(search):
	if count(search) != 1:
		try:
			os.mkdir(htmldir)
		except OSError:
			pass
		
		html = open(htmldir + search + ".html", "w+")
		html.write("<p>" +  "Artikel Heute mit" + search + ": " + str(count(search)) + "</p>\n")
		html.write("<p>" + "" + "</p>\n")
		html.write("<p>" +  "Schlagzeilen Heute:" + "</p>\n")
		html.write("<p>" + "" + "</p>\n")
		title(search, html)
		html.write("<p>" + "" + "</p>\n")
		html.write("<p>" +  "Archiv:" + "</p>\n")
		html.write("<p>" + "" + "</p>\n")
		archiv(search, html)
