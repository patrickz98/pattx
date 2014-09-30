#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import time
import re
import conf

def main(data):
	con = conf.con

	with con:
    
	    cur = con.cursor()
	    cur.execute("DROP TABLE IF EXISTS data%s" % str(time.strftime("%Y%m%d")))
	    cur.execute("CREATE TABLE data%s(Word VARCHAR(30), Cluster VARCHAR(4))" % str(time.strftime("%Y%m%d")))
    
    	for word in data:
	    	cur.execute("INSERT INTO data%s(Word, Cluster) VALUES('%s', %d)" % \
	    		(str(time.strftime("%Y%m%d")), word, data[word]))

		con.commit()
	
	con.close()

def raw(data):
	con = mdb.connect('odroid-u3.local', 'monitor', 'test123', 'monitor')

	with con:
    
	    cur = con.cursor()
	    cur.execute("DROP TABLE IF EXISTS news%s" % str(time.strftime("%Y%m%d")))
	    cur.execute("CREATE TABLE news%s(Headlines VARCHAR(200), Newspaper VARCHAR(20), link VARCHAR(200))" % str(time.strftime("%Y%m%d")))
	        	
    	for news in data:
	    	cur.execute("INSERT INTO news%s(Headlines, Newspaper) VALUES('%s', '%s')" % \
	    		(str(time.strftime("%Y%m%d")), news, data[news]))

		con.commit()
	
	con.close()