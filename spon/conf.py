#!/usr/bin/python
import os

dir =  "./words/"
htmldir = "./html/"

#text = ["news-spon.txt", "news-welt.txt", "news-zeit.txt", 
#		"news-stern.txt", "news-faz.txt", "news-ntv.txt", 
#		"news-tagesspiegel.txt", "news-sueddeutsche.txt"]

text = [x for x in os.listdir(".") if "news-" in x]