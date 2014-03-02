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

#192.168.0.1

# Rechner

#first_num=0
#second_num=0

#echo -n "Enter the first number --> "
#read first_num
#echo -n "Enter the second number -> "
#read second_num

#echo "first number + second number = $((first_num + second_num))"
#echo "first number - second number = $((first_num - second_num))"
#echo "first number * second number = $((first_num * second_num))"
#echo "first number / second number = $((first_num / second_num))"
#echo "first number % second number = $((first_num % second_num))"
#echo "first number raised to the"
#echo "power of the second number   = $((first_num ** second_num))"


# if mit Zietbegränzung 

#echo -n "Hurry up and type something! > "          
#if read -t 3 response; then                  
#    echo "Great, you made it in time!"
#else
#    echo "Sorry, you are too slow!"
#fi


#Wen Enter dan @@@

#read -n1 KEY ##### Wen Enter dan @@@
#if [[ "$KEY" == "" ]]
#then
#  echo "@@@";
#fi


#echo Hallo, user, alles in Ordnung?
#echo Ihre Antwort, n/j:
#read answer
#echo Ihre Antwort war: $answer
# if [ "$answer" = "j" ]
#if [ "$answer" != "n" ]
#  then echo ja
#  else echo nein
#fi  

