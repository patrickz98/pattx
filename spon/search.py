
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re
import regex
import spon, zeit, welt, stern, faz


spon.spon()
zeit.zeit()
welt.welt()
stern.stern()
faz.faz()
regex.main()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", "news-stern.txt"]

def title(word):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               print txt[5:-4] + "= " + a[:-1]


search = raw_input("Suche: ")
title(search)
