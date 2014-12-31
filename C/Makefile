all:
	gcc args.c -o args -std=gnu99
	gcc ascii.c -o ascii
	gcc char.c -o char
	gcc client.c -o client
	gcc curl.c -o curl -lcurl
	gcc echo.c -o echo
	gcc filereader.c -o filereader
	gcc filewriter.c -o filewriter
	gcc hallo.c -o hallo
	gcc server.c -o server
	gcc sound.c -o sound
	gcc speicher.c -o speicher
	gcc std.c -o std
	gcc string.c -o string
	gcc string2.c -o string2
	gcc test.c -o test
	gcc rand.c -o rand
	gcc -Iinclude.h class.c -o class
	gcc string3.c -o string3

clean:
	python help.py clean

list:
	python help.py list

default: all
