all:
	gcc args.c -o args -std=gnu99
	gcc ascii.c -o ascii
	gcc char.c -o char
	gcc client.c -o client
	gcc daten_ein.c -o daten_ein
	gcc daten_ein_mehrere.c -o daten_ein_mehrere
	gcc echo.c -o echo
	gcc filereader.c -o filereader
	gcc filewriter.c -o filewriter
	gcc hallo.c -o hallo
	gcc server.c -o server
	gcc sound.c -o sound
	gcc std.c -o std
	gcc string.c -o string
	gcc test.c -o test
	gcc -lcurl curl.c -o curl

clean:
	python help.py clean

default: all
