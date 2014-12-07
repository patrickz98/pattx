JFLAGS = -g
JC = javac
.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	./aktien.java \
	./awt.java \
	./example.java \
	./file.java \
	./graph.java \
	./hallo.java \
	./html.java \
	./keyfile.java \
	./klassen.java \
	./klassen2.java \
	./Multi.java \
	./random.java \
	./read.java \
	./regex.java \
	./shell.java \
	./SSLTCPClient.java \
	./SSLTCPServer.java \
	./swing.java \
	./TCPClient.java \
	./TCPdata.java \
	./TCPServer.java \
	./TCPServerdata.java

default: classes

classes: $(CLASSES:.java=.class)

clean:
	find . -name "*.class" -delete;
