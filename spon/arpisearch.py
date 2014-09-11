
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

import regex
import spon, zeit, welt, stern, faz, ntv, tagesspiegel, sueddeutsche
import conf

spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
ntv.ntv()
tagesspiegel.tagesspiegel()
sueddeutsche.sueddeutsche()
regex.main()

text = conf.text

def count(word):
        count = 0
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                                count = count + 1
        return count


def title(word):
        list = []
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               list.append( a[:-1] + (" (%s)" % txt[5:-4]))
        return list

def main(search):
#	search = raw_input("Suche: ")
	list = []
	list.append( "Artikel mit " + search + ": " + str(count(search)))
	list = list + title(search)

	return list