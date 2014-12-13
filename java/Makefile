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
	./FileReceiver.java \
	./FileSender.java \
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
	./sslclient.java \
	./ssldata.java \
	./ssldataserver.java \
	./sslserver.java \
	./swing.java \
	./TCPClient.java \
	./TCPdata.java \
	./TCPServer.java \
	./TCPServerdata.java \
	./test.java \
	./test2.java

default: classes

classes: $(CLASSES:.java=.class)

clean:
	find . -name "*.class" -delete;

all:
	find . -name "*.java" -exec javac -g "{}" \; -exec echo "javac "{} \;

git: clean
	cp * ../pattx/java/
	cd ../pattx/; git add java/*; git commit -a; git push

list:
	find . -name "*.java" -exec echo "{}"" \\" \;
	
chat:
	javac Chat.java;
	javac info.java;
	jar cf chat.jar Chat.class client.class host.class info.class mySrvKeystore;