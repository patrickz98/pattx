uname = `uname`	

all:
	python analytics.py > aktuell.txt
	python grapher.py > statistik.txt
	python grapher-html.py > statistik.html

clean:
	rm news-*
	rm *.pyc
	rm data-raw.txt
	rm statistik.txt
	rm aktuell.txt

web: all
	sudo cp statistik.txt aktuell.txt statistik.html /var/www/patrickz/
	sudo cp statistik.txt aktuell.txt statistik.html /var/www/odroid/

	sudo chown www-data:www-data /var/www/patrickz/statistik.txt
	sudo chown www-data:www-data /var/www/patrickz/aktuell.txt

	sudo chown www-data:www-data /var/www/odroid/statistik.txt
	sudo chown www-data:www-data /var/www/odroid/aktuell.txt
	
	sudo chown www-data:www-data /var/www/patrickz/statistik.html
	sudo chown www-data:www-data /var/www/odroid/statistik.html

nohup:
	nohup sudo python web.py 1>/dev/null 2>/dev/null &

words:
	ifeq ("$(uname)" == "Darwin"); then \
		scp odroid@odroid-u3.local:~/Core/pattx/spon/words/* words/; \
	else \
		scp patrick@patrick-macbook.local:~/github/patrickzyolo/spon/words/* words/; \
	endif; \
