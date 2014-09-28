#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import time
import os
import re

import conf

dir = conf.dir
def main():
	con = mdb.connect('odroid-u3.local', 'monitor', 'test123', 'monitor')

	for txt in os.listdir(dir):
		if "news-" in txt:
			text = open(dir + txt, "r")
		
			txt = txt[:-4]
			while '.' in txt:
				txt = txt.replace('.','')
		
			while '-' in txt:
				txt = txt.replace('-','')
		
				
			with con:
		
				cur = con.cursor()
    			cur.execute("DROP TABLE IF EXISTS %s" % txt)
    			cur.execute("CREATE TABLE %s(Headlines VARCHAR(200), Newspaper VARCHAR(20))" % txt)
    
    			for news in text:
    				if '\'' in news:
						news = news.replace('\'','')
			
				news = re.findall("(.*?)\((.*?)\)", news)
			
				print txt, "-->", news[0][0], "(" + news[0][1] + ")"
    		
    				cur.execute("INSERT INTO %s(Headlines, Newspaper) VALUES('%s', '%s')" % \
    					(txt, news[0][0], news[0][1]))

				con.commit()	
	con.close()

main()
