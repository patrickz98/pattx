#!/usr/bin/python
import os
import time

while(True):
	os.popen("make web").readlines()
	time.sleep(3600)
