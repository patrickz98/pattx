#!/usr/bin/python
import os

svctags = ["JNX58Z1", "CLH4L4J", "CLKZX3J", "5YXFWX1", "JYXFWX1", "CD27K4J"]
apikey = "849e027f476027a394edd656eaef4842"

for x in svctags:
	api = str(os.popen('curl "https://api.dell.com/support/v2/assetinfo/warranty/tags.xml?svctags=%s&apikey=%s" \
			2>/dev/null' % (x, apikey)).readlines())

	while(True):
		if "<a:EndDate>" in api:
			part1 = api.find("<a:EndDate>") + 11
			part2 = api.find("</a:EndDate>")
			print x + " EndDate: " + api[part1:part2]
			api = api[api.find("</a:EndDate>") + 11:]
		else:
#			print
			break

	while(True):
                if "<a:ServiceLevelDescription>" in api:
                        part1 = api.find("<a:ServiceLevelDescription>") + len("<a:ServiceLevelDescription>")
                        part2 = api.find("</a:ServiceLevelDescription>")
                        print x + " ServiceLevelDescription: " + api[part1:part2]
                        api = api[api.find("</a:ServiceLevelDescription>") + len("<a:ServiceLevelDescription>"):]
                else:
                        print
                        break
