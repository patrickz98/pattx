JFLAGS = -g
JC = javac
.SUFFIXES: .java .class

.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	./aktien.java \
	./awt.java \
	./Chat.java \
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
	./SSL.java \
	./SSLTCPClient.java \
	./SSLTCPServer.java \
	./swing.java \
	./TCPClient.java \
	./TCPdata.java \
	./TCPServer.java \
	./TCPServerdata.java \
	./test.java 

default: classes

classes: $(CLASSES:.java=.class)

clean:
	find . -name "*.class" -delete;
	
all:
	find . -name "*.java" -exec javac "{}" \;

clean:
	find . -name "*.class" -delete;

git: clean
	cp * ../pattx/java/
	cd ../pattx/; git add java/*; git commit -a; git push

