tarc:
	tar -cvzf BuringSeries.gz BuringSeries/
	tar -cvzf Guardian.gz     Guardian/
	tar -cvzf Times.gz        Times/
	tar -cvzf Pons.gz         Pons/

tarx:
	tar -xvzf BuringSeries.gz
	tar -xvzf Guardian.gz
	tar -xvzf Times.gz
	tar -xvzf Pons.gz

decrypt:
	openssl aes-256-cbc -d -a -in BuringSeries.gz.cry -out BuringSeries.gz -kfile passwd.txt
	openssl aes-256-cbc -d -a -in Guardian.gz.cry     -out Guardian.gz     -kfile passwd.txt
	openssl aes-256-cbc -d -a -in Times.gz.cry        -out Times.gz        -kfile passwd.txt
	openssl aes-256-cbc -d -a -in Pons.gz.cry         -out Pons.gz         -kfile passwd.txt

encrypt: tarc
	openssl aes-256-cbc -e -a -in BuringSeries.gz -out BuringSeries.gz.cry -kfile passwd.txt
	openssl aes-256-cbc -e -a -in Guardian.gz     -out Guardian.gz.cry     -kfile passwd.txt
	openssl aes-256-cbc -e -a -in Times.gz        -out Times.gz.cry        -kfile passwd.txt
	openssl aes-256-cbc -e -a -in Pons.gz         -out Pons.gz.cry         -kfile passwd.txt

encrypt-google:
	openssl aes-256-cbc -e -a -in google.txt -out google.txt.cry -kfile passwd.txt

decrypt-google:
	openssl aes-256-cbc -d -a -in google.txt.cry -out google.txt -kfile passwd.txt

update: clean encrypt encrypt-google
	rm -rf BuringSeries.gz
	rm -rf Guardian.gz
	rm -rf Times.gz
	rm -rf Pons.gz

	rm -rf BuringSeries
	rm -rf Guardian
	rm -rf Times
	rm -rf Pons

	rm -rf google.txt

update-dec: decrypt tarx decrypt-google clean-gz clean-aes


clean:
	find . -name ".*DS_Store" -delete

clean-gz:
	rm -rf BuringSeries.gz
	rm -rf Guardian.gz
	rm -rf Times.gz
	rm -rf Pons.gz

clean-aes:
	rm -rf BuringSeries.gz.cry
	rm -rf Guardian.gz.cry
	rm -rf Times.gz.cry
	rm -rf Pons.gz.cry

	rm -rf google.txt.cry
