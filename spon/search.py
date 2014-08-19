
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import regex
import spon, zeit, welt, stern, faz, ntv


spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
ntv.ntv()
regex.main()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", "news-stern.txt", "news-faz.txt", "news-ntv.txt"]

def title(word):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               print a[:-1] + (" (%s)" % txt[5:-4])


search = raw_input("Suche: ")
title(search)
