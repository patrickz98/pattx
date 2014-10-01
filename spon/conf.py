#!/usr/bin/python
import os
import MySQLdb as mdb
import data

dir =  "./words/"
htmldir = "./html/"
text = [x for x in os.listdir(".") if "news-" in x]
data = data.main()
#con = mdb.connect('odroid-u3.local', 'monitor', 'test123', 'monitor')