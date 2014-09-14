#!/usr/bin/python
import re
import time

import data

def graph(word, text):
	dataori = text	
	data = []
	for z in dataori:
		if z not in data and not z == '\n' and z[:z.index(":")] == word:
			data.append(z)
	
	size = []
	for a in data:
		find = re.findall(".*: (.*?) date:", a)
		size.append(int(''.join(find)))

	if len(size) >= 2:
		print "		<h1>" + word + "</h1>"
	
		print '		<div style="width:60%">'
		print '			<div>'
		print '				<canvas id="%s" height="450" width="600"></canvas>' % word
		print '			</div>'
		print '		</div>'

		javascript.append( '			var randomScalingFactor = function(){ return Math.round(Math.random()*100)};')
		javascript.append( '			var lineChartData%s = {' % word )
		javascript.append( '				labels : %s,' % (date(word, text)) )
		javascript.append( '				datasets : [' )
		javascript.append( '					{' )
		javascript.append( '						label: "%s",' % word )
		javascript.append( '						fillColor : "rgba(151,187,205,0.2)",' )
		javascript.append( '						strokeColor : "rgba(151,187,205,1)",' )
		javascript.append( '						pointColor : "rgba(151,187,205,1)",' )
		javascript.append( '						pointStrokeColor : "#fff",' )
		javascript.append( '						pointHighlightFill : "#fff",' )
		javascript.append( '						pointHighlightStroke : "rgba(151,187,205,1)",' )
		javascript.append( '						data : %s' % ''.join(str(size)) )
		javascript.append( '					}' )
		javascript.append( '				]' )
		javascript.append( '			}' )
		javascript.append( '' )

		javaconf.append( '				var ctx%s = document.getElementById("%s").getContext("2d");' % (word, word) )
		javaconf.append( '				window.myLine%s = new Chart(ctx%s).Line(lineChartData%s, {' % (word, word, word) )
		javaconf.append( '				responsive: true });' )
		

def date(word, text):
	data = text
	nown = []
	end = []

	for txt in data:
		line = txt[:txt.index(":")]
		if line == word and txt not in nown:
			end.append(txt[-10:])
			nown.append(txt)
	
	return end

javascript = ['		<script>']
javaconf = []

def main():
	text = data.main()
	words = []
	
	for line in text:
		if not line[:line.index(":")] in words:
			words.append(line[:line.index(":")])

	print '<!doctype html>'
	print '<html>'
	print '	<head>'
	print '		<title>Line Chart</title>'
	print '		<script src="./Chart.js"></script>'
	print '</head>'
	print '<body>'
	print '		<div>' + time.strftime('%H:%M %d.%m.%Y') + '</div>'

	words = ["Merkel", "Obama", "Ukraine", "Staat", 
			 "Russland", "Kiew", "Europa", "Krise", 
			 "Kurden", "Polizei", "Kampf"]

	for w in words:
		graph(w, text)

	javascript.append( '			window.onload = function(){' )
	
	for conf in javaconf:
		javascript.append(conf)
	
	javascript.append( '			}' )
	javascript.append( '		</script>' )	

	for java in javascript:
		print java
	
	print "</body>"
	print "</html>"
main()