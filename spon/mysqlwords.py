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
	con = conf.con

	for txt in os.listdir(dir):
		if ".data" in txt:
			text = open(dir + txt, "r")
		
			txt = txt[:-5]
			while '.' in txt:
				txt = txt.replace('.','')
		
			while '-' in txt:
				txt = txt.replace('-','')
		
			print txt

			with con:
		
				cur = con.cursor()
    			cur.execute("DROP TABLE IF EXISTS data%s" % txt)
    			cur.execute("CREATE TABLE data%s(Word VARCHAR(200), Cluster VARCHAR(20))" % txt)
    
    			for news in text:
    				if '\'' in news:
						news = news.replace('\'','')
			
				news = re.findall("(.*?):(.*)", news)
			
				print txt, "-->", news[0][0], news[0][1]
    		
    				cur.execute("INSERT INTO data%s(Word, Cluster) VALUES('%s', '%s')" % \
    					(txt, news[0][0], news[0][1]))

				con.commit()	
	con.close()

main()
