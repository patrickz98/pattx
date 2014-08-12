#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'testuser', 'test623', 'testdb');

with con:
    
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Writers")
    cur.execute("CREATE TABLE Writers(bla VARCHAR(20), huhu VARCHAR(20), test VARCHAR(20))")
    cur.execute("INSERT INTO Writers(bla, huhu, test) VALUES('Jack London', 'Jack London', 'Jack London')")
    cur.execute("INSERT INTO Writers(bla) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(bla) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(bla) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(bla) VALUES('Truman Capote')")

    cur.execute("INSERT INTO Writers(huhu) VALUES('Jack London')")
    cur.execute("INSERT INTO Writers(huhu) VALUES('Honore de Balzac')")
    cur.execute("INSERT INTO Writers(huhu) VALUES('Lion Feuchtwanger')")
    cur.execute("INSERT INTO Writers(huhu) VALUES('Emile Zola')")
    cur.execute("INSERT INTO Writers(huhu) VALUES('Truman Capote')")

