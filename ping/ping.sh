#!/bin/sh



echo Web/IP ?
read www

if [ "$www" = "Web" ]
	then echo Adresse ?
	read wwwadresse

	echo Anzahl Pings
	read zahl

	ping -c $zahl $wwwadresse | grep received
	#read wwwanswer

fi

if [ "$www" = "ip" ]

	then echo IP Adresse: Lan/Web ?
	read 1
		if [ "$1" = "lan" ]
			then echo 192.168.0.???
				read ipadresse
				echo Pings
				read anzahl

				ping -c $anzahl 192.168.0.$ipadresse  | grep received
				#read ipanswer
		fi

		if [ "$1" = "web " ]
	        	then echo Adresse
	        	read ipadresse
	        	echo Pings
	        	read anzahl

	        	ping -c $anzahl $ipadresse  | grep received
	        	read ipanswer
		fi

fi
