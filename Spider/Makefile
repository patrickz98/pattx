tarc:
	tar -cvzf Guardian.gz Guardian/
	tar -cvzf Pons.gz     Pons/

tarx:
	tar -xvzf Guardian.gz
	tar -xvzf Pons.gz

decrypt:
	openssl aes-256-cbc -d -in Guardian.gz.aes -out Guardian.gz
	openssl aes-256-cbc -d -in Pons.gz.aes     -out Pons.gz

encrypt: tarc
	openssl aes-256-cbc -in Guardian.gz -out Guardian.gz.aes
	openssl aes-256-cbc -in Pons.gz     -out Pons.gz.aes
