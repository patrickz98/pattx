all:
	g++ hallo.cpp -o hallo
	g++ stdin.cpp -o stdin
	g++ classes.cpp -o classes

static:
	g++ -c class.cpp -o AddNumbers.o
	ar rcs libAddNumbers.a AddNumbers.o

shared:
	g++ -fpic -c class.cpp -o AddNumbers.o
	g++ -shared -o libAddNumbers.so AddNumbers.o

clean:
	python help.py clean

default: all
