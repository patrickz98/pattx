all:
	find . -name "*.java" -exec javac "{}" \;

clean:
	find . -name "*.class" -delete;

git: clean
	cp * ../pattx/java/
	cd ../pattx/; git add java/*; git commit -a

