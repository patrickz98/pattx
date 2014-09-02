all:
	python analytics.py > aktuell.txt
	python grapher.py > statistik.txt

clean:
	rm news-*
	rm *.pyc
	rm data-raw.txt
	rm statistik.txt
	rm aktuell.txt

web: all
	sudo cp statistik.txt aktuell.txt /var/www/patrickz/

nohup:
	nohup sudo python web.py 1>/dev/null 2>/dev/null &

words:
	scp patrick@patrick-macbook.local:~/github/patrickzyolo/spon/words/* .

