#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import re

import conf
import data
import regex

dir = conf.dir 
text = conf.text
htmldir = conf.htmldir

def count(word):
        count = 0
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                                count = count + 1
        return count

def date(word, text):
	nown = []
	end = []

	for txt in text:
		line = txt[:txt.index(":")]
		if line == word and txt not in nown:
			end.append(txt[-10:])
			nown.append(txt)
	
	return end

def title(word, html):
        for txt in text:
                tx = open(txt, "r").readlines()
                for a in tx:
                        if word in a:
                               html.write("<p>" +  a[:-1] + (" (%s)" % txt[5:-4]) + "</p>\n")

def archiv(word, html):
	archiv = sorted(os.listdir(dir))
	archiv = [conf.dir + x for x in archiv if "news-" in x and not time.strftime("%Y.%m.%d") in x]
	for txt in archiv:
		tx = open(txt, "r").readlines()
		for a in tx:
			if word in a:
				html.write("<p>" +  a[:-1] + (" (%s)" % txt[13:-4]) + "</p>\n")

def graph(word, text, html):
	data = []
	for z in text:
		if z not in data and not z == '\n' and z[:z.index(":")] == word:
			data.append(z)
	
	size = []
	for a in data:
		find = re.findall(".*: (.*?) date:", a)
		size.append(int(''.join(find)))

	if len(size) >= 5:
	
		html.write('		<div style="width:60%">\n')
		html.write('			<div>\n')
		html.write('				<canvas id="%s" height="450" width="600"></canvas>\n' % word)
		html.write('			</div>\n')
		html.write('		</div>\n')
		html.write('\n')
		
		html.write( '		<script>\n' )	
		html.write( '			var randomScalingFactor = function(){ return Math.round(Math.random()*100)};\n')
		html.write( '			var lineChartData%s = {\n' % word )
		html.write( '				labels : %s,\n' % (date(word, text)) )
		html.write( '				datasets : [\n' )
		html.write( '					{\n' )
		html.write( '						label: "%s",\n' % word )
		html.write( '						fillColor : "rgba(151,187,205,0.2)",\n' )
		html.write( '						strokeColor : "rgba(151,187,205,1)",\n' )
		html.write( '						pointColor : "rgba(151,187,205,1)",\n' )
		html.write( '						pointStrokeColor : "#fff",\n' )
		html.write( '						pointHighlightFill : "#fff",\n' )
		html.write( '						pointHighlightStroke : "rgba(151,187,205,1)",\n' )
		html.write( '						data : %s\n' % ''.join(str(size)) )
		html.write( '					}\n' )
		html.write( '				]\n' )
		html.write( '			}\n' )
		html.write( '\n' )
		html.write( '			window.onload = function(){\n')
		html.write( '				var ctx%s = document.getElementById("%s").getContext("2d");\n' % (word, word) )
		html.write( '				window.myLine%s = new Chart(ctx%s).Line(lineChartData%s, {\n' % (word, word, word) )
		html.write( '				responsive: true, animation: false });\n' )
		html.write( '			}\n' )
		html.write( '		</script>\n' )
		
	else:
	
		return False

def main(search):
	if count(search) != 1:
		try:
			os.mkdir(htmldir)
		except OSError:
			pass
		
		while '"' in search:
			search.remove('"')
		
		text = data.main()
		html = open(htmldir + search + ".html", "w+")
		
		html.write('<!doctype html>\n')
		html.write('<html>\n')
		html.write('	<head>\n')
		html.write('		<title>%s</title>\n' % search)
		html.write('		<link rel="icon" type="image/x-icon" href="news.ico" />\n')
		html.write('		<link rel="apple-touch-icon" href="news.png"/>')
		html.write('		<script src="../Chart.js"></script>\n')
		html.write('\n')
		html.write('</head>\n')
		html.write('<body>\n')
		html.write('<h1>' + search + '</h1>\n')
		html.write("<p>" +  "Artikel Heute mit " + search + ": " + str(count(search)) + "</p>\n")
		html.write("<p></p>\n")
		
		graph(search, text, html)
		
		html.write("<h3>" +  "Schlagzeilen Heute:" + "</h3>\n")
		html.write("<p></p>\n")
		title(search, html)
		html.write("<p></p>\n")
		html.write("<h3>" +  "Archiv:" + "</h3>\n")
		html.write("<p></p>\n")
		archiv(search, html)
		
		html.write("</body>\n")
		html.write("</html>\n")
		
		html.close()
