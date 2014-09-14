uname = `uname`	

all:
	python analytics.py > aktuell.txt
	python grapher.py > statistik.txt
	python grapher-html.py

clean:
	rm news-*
	rm *.pyc
	rm statistik.txt
	rm aktuell.txt
	rm statistik.html

web: all
	sudo cp statistik.txt aktuell.txt statistik.html /var/www/patrickz/
	sudo cp statistik.txt aktuell.txt statistik.html /var/www/odroid/

	sudo chown www-data:www-data /var/www/patrickz/statistik.txt
	sudo chown www-data:www-data /var/www/odroid/statistik.txt

	sudo chown www-data:www-data /var/www/patrickz/aktuell.txt
	sudo chown www-data:www-data /var/www/odroid/aktuell.txt
	
	sudo chown www-data:www-data /var/www/patrickz/statistik.html
	sudo chown www-data:www-data /var/www/odroid/statistik.html

nohup:
	nohup sudo python web.py 1>/dev/null 2>/dev/null &

mac:
	scp odroid@odroid-u3.local:~/Core/pattx/spon/words/* words/; \

lib:
	git clone https://github.com/nnnick/Chart.js.git
	cd Chart.js; git pull
	
	sudo cp Chart.js/Chart.js /var/www/patrickz/
	sudo cp Chart.js/Chart.js /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/Chart.js
	sudo chown www-data:www-data /var/www/odroid/Chart.js

	sudo cp news.ico /var/www/patrickz/
	sudo cp news.ico /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/news.ico
	sudo chown www-data:www-data /var/www/odroid/news.ico

backup:
	tar cvzf words.gz words/
	zip words.zip words/*