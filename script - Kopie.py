#!/usr/bin/python

zoo_animals = ["pangolin", "cassowary", "sloth", ];
print len(zoo_animals)
print zoo_animals[0]

import os
dir = os.popen("ls -al").readlines()
print dir

from datetime import datetime 

now = datetime.now()
print now
print now.year
print now.month
print now.day

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)

fifth_letter = "MONTY"

print fifth_letter[4]

string_1 = "Camelot"
string_2 = "place"

print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

name = raw_input("What is your name? ")
color = raw_input("What is your favorite color? ")

print "Ah, so your name is %s " \
"and your favorite color is %s." % (name, color)

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")     # Use index() to find "duck"

animals.insert(duck_index, "cobra")

my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print 2 * number

