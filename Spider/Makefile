tarc:
	cd Guardian/; make clean
	cd Pons/;     make clean

	tar -cvzf Guardian.gz Guardian/
	tar -cvzf Pons.gz     Pons/

tarx:
	tar -xvzf Guardian.gz
	tar -xvzf Pons.gz

decrypt:
	openssl aes-256-cbc -d -a -in Guardian.gz.aes -out Guardian.gz
	openssl aes-256-cbc -d -a -in Pons.gz.aes     -out Pons.gz

encrypt: tarc
	openssl aes-256-cbc -e -a -in Guardian.gz -out Guardian.gz.aes
	openssl aes-256-cbc -e -a -in Pons.gz     -out Pons.gz.aes

update: encrypt
	rm -rf Guardian.gz
	rm -rf Pons.gz

clean:
	rm -rf Guardian.gz
	rm -rf Pons.gz

	rm -rf Guardian.gz.aes
	rm -rf Pons.gz.aes

	rm -rf times.txt.aes
	rm -rf google.txt.aes

encrypt-stuff:
	openssl aes-256-cbc -e -a -in times.txt  -out times.txt.aes
	openssl aes-256-cbc -e -a -in google.txt -out google.txt.aes

decrypt-stuff:
	openssl aes-256-cbc -d -a -in times.txt.aes  -out times.txt
	openssl aes-256-cbc -d -a -in google.txt.aes -out google.txt.
