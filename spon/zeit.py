#!/usr/bin/python
import re
from urllib2 import Request, urlopen, URLError
import conf
import time

def zeit():
	schlagzeilen = open("news-zeit.txt", "w+")
	request = Request('http://www.zeit.de/news/index')

	try:
		response = urlopen(request)
		html = response.read()
	except URLError, e:
	    print 'Error:', e

	find = re.findall("<a href=\"(.*?)\".*?<strong>(.*?)</strong> <span>(.*?)</span>", html)

# 	con = conf.con
# 
# 	with con:
#     
# 	    cur = con.cursor()
# 	    cur.execute("DROP TABLE IF EXISTS news%s" % str(time.strftime("%Y%m%d")))
# 	    cur.execute("CREATE TABLE news%s(Headlines VARCHAR(200), Newspaper VARCHAR(20), link VARCHAR(200))" % str(time.strftime("%Y%m%d")))
# 	    
#     	    for word in find:
# 		print word
# 
#     		if "\"" in word: 
#     			word = re.sub(r"\"", "", word)
#     		if "'" in word: 
#     			word = re.sub(r"'", "", word)
# 			
# 			
# 	    	cur.execute("INSERT INTO news%s(Headlines, Newspaper, link) VALUES('%s', '%s', '%s')" % \
# 	    		(str(time.strftime("%Y%m%d")), word[1] + ": " + word[2], 'zeit', word[0]))
# 
# 		con.commit()
# 		con.close()

	for i in find:
		#print i[0] link
		schlagzeilen.write(i[1] + ": " + i[2] + "\n")

	schlagzeilen.close()
