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
		print "<h1>" + word + "</h1>"

		print '		<script>'
		print '			var randomScalingFactor = function(){ return Math.round(Math.random()*100)};'
		print '			var lineChartData = {'
		print '				labels : ["January","February","March","April","May","June","July"],'
		print '				datasets : ['
		print '					{'
		print '						label: "My Second dataset",'
		print '						fillColor : "rgba(151,187,205,0.2)",'
		print '						strokeColor : "rgba(151,187,205,1)",'
		print '						pointColor : "rgba(151,187,205,1)",'
		print '						pointStrokeColor : "#fff",'
		print '						pointHighlightFill : "#fff",'
		print '						pointHighlightStroke : "rgba(151,187,205,1)",'
		print '						data : [%s]' % size
		print '					}'
		print '				]'
		print '			}'
		print ''
		print '			window.onload = function(){'
		print '				var ctx = document.getElementById("canvas").getContext("2d");'
		print '				window.myLine = new Chart(ctx).Line(lineChartData, {'
		print '				responsive: true'
		print '				});'
		print '			}'
		print '		</script>'	

		date(word, text)

def date(word, text):
	data = text
	nown = []
	count = 1

	for txt in data:
		line = txt[:txt.index(":")]
		if line == word and txt not in nown:
			print "<div>" + str(count) + ":&nbsp;" + txt + "</div>"
			nown.append(txt)
			count = count + 1

def main():
	text = data.main()
	words = []

	print '<!doctype html>'
	print '<html>'
	print '	<head>'
	print '		<title>Line Chart</title>'
	print '		<script src="../Chart.js"></script>'
	print '</head>'
	print '<body>'
	print '		<div>' + time.strftime('%H:%M %d.%m.%Y') + '</div>'
	print '		<div style="width:30%">'
	print '			<div>'
	print '				<canvas id="canvas" height="450" width="600"></canvas>'
	print '			</div>'
	print '		</div>'


	for line in text:
		if not line[:line.index(":")] in words:
			words.append(line[:line.index(":")])

	for w in words:
		graph(w, text)
	print "</body>"
	print "</html>"
main()