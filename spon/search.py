
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

os.popen("python spon.py").readlines()
os.popen("python zeit.py").readlines()
os.popen("python welt.py").readlines()
os.popen("python stern.py").readlines()
#os.popen("python faz.py").readlines()

text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", "news-stern.txt"]

def title(word):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               print txt[5:-4] + "= " + a[:-1]


search = raw_input("Suche: ")
title(search)
