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
sueddeutsche.sueddeutsche()
regex.main()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", 
		"news-stern.txt", "news-faz.txt", "news-ntv.txt", 
		"news-tagesspiegel.txt", "news-sueddeutsche.txt"]
	
def count(word):
        count = 0
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                                count = count + 1
        return count


def title(word):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               print a[:-1] + (" (%s)" % txt[5:-4])

def archiv(word):
	archiv = sorted(os.listdir(conf.dir))
	archiv = [conf.dir + x for x in archiv if "news-" in x]
	for txt in archiv:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				print a[:-1] + (" (%s)" % txt[13:-4])

search = raw_input("Suche: ")
print "Artikel mit " + search + ": " + str(count(search))
print
arpigrapher.graph(search)
print "Schlagzeilen:"
print
title(search)
print "Archiv:"
print
archiv(search)