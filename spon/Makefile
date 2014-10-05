uname = `uname`	

all:
	python analytics.py > aktuell.txt
	python grapher.py > statistik.txt
	python analytics-html.py

clean:
	rm news-*
	rm *.pyc
	rm statistik.txt
	rm aktuell.txt
	rm statistik.html
	rm statistik-all.html
	rm aktuell.html
	rm -rf html

mysql:
	cd ../../monitor/; make mysql;

web: chown all mysql
	sudo cp statistik.txt aktuell.txt aktuell.html /var/www/patrickz/
	sudo cp statistik.txt aktuell.txt aktuell.html /var/www/odroid/

	sudo cp -r html /var/www/patrickz/
	sudo cp -r html /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/html/
	sudo chown www-data:www-data /var/www/odroid/html/
	
	sudo chown www-data:www-data /var/www/patrickz/html/*
	sudo chown www-data:www-data /var/www/odroid/html/*
	
	sudo chown www-data:www-data /var/www/patrickz/statistik.txt
	sudo chown www-data:www-data /var/www/odroid/statistik.txt

	sudo chown www-data:www-data /var/www/patrickz/aktuell.txt
	sudo chown www-data:www-data /var/www/odroid/aktuell.txt
		
	sudo chown www-data:www-data /var/www/patrickz/aktuell.html
	sudo chown www-data:www-data /var/www/odroid/aktuell.html

nohup:
	sudo nohup python web.py 1>/dev/null 2>/dev/null &

mac:
	curl "https://raw.githubusercontent.com/nnnick/Chart.js/master/Chart.js" 1> Chart.js 2>/dev/null
	scp odroid@odroid-u3.local:~/Core/pattx/spon/words/* words/

lib:
	wget https://raw.githubusercontent.com/nnnick/Chart.js/master/Chart.js
	
	sudo cp Chart.js/Chart.js /var/www/patrickz/
	sudo cp Chart.js/Chart.js /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/Chart.js
	sudo chown www-data:www-data /var/www/odroid/Chart.js

	sudo cp news.ico /var/www/patrickz/
	sudo cp news.ico /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/news.ico
	sudo chown www-data:www-data /var/www/odroid/news.ico
	
	sudo cp news.png /var/www/patrickz/
	sudo cp news.png /var/www/odroid/
	
	sudo chown www-data:www-data /var/www/patrickz/news.png
	sudo chown www-data:www-data /var/www/odroid/news.png

backup:
	tar cvzf words.gz words/
	zip words.zip words/*

chown:
	sudo chown odroid:odroid words/*
	sudo chown odroid:odroid html/*

webclean:
	sudo rm -rf /var/www/patrick/statistik.txt
	sudo rm -rf /var/www/odroid/statistik.txt
	
	sudo rm -rf /var/www/patrick/aktuell.txt
	sudo rm -rf /var/www/odroid/aktuell.txt

	sudo rm -rf /var/www/patrick/statistik.html
	sudo rm -rf /var/www/odroid/statistik.html
	
	sudo rm -rf /var/www/patrick/statistik-all.html
	sudo rm -rf /var/www/odroid/statistik-all.html
	
	sudo rm -rf /var/www/patrick/aktuell.html
	sudo rm -rf /var/www/odroid/aktuell.html
	
	sudo rm -rf /var/www/patrick/html
	sudo rm -rf /var/www/odroid/html