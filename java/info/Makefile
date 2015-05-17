default: all

clean:
	find . -name "*.class" -delete;

all:
	find . -name "*.java" -exec javac -g "{}" \; -exec echo "javac "{} \;

list:
	find . -name "*.java" -exec echo "{}"" \\" \;
