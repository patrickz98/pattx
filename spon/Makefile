all:
	python analytics.py > aktuell.txt
	python grapher.py > statistik.txt

clean:
	rm news-*
	rm *.pyc
	rm data-raw.txt
	rm statistik.txt

web: all
	sudo cp statistik.txt aktuell.txt /var/www/patrickz/
