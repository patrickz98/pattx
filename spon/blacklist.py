#!/usr/bin/python
# -*- coding: utf-8 -*-

bad = ["um", "an", "von", "in", "den", "haelt", "sicher", "tritt", "essen",
       "im", "die", "mit", "bei", "sich", "offen", "Leute", "Fuenf", "echt",
       "des", "Die", "der", "ab", "am", "legt", "laenger", "zeigt", "lang", "gibt",
       "-", "und", "auf", "zum", "Der", "Woche", "Jahren", "kein", "euch", "Kein",
       "vor", ":", "ist", "zum", "eine", "zu", "aus", "muss", "oben", "haben",
       "ein", "er", "ich", "so", "es", "ter", "zur", "laesst", "startet", "Video",
       "Ja", "in", "Ab", "Im", "dem", "ja", "wer", "du", "ein", "unter", "here",
       "er", "war", "Er", "tun", "als", "hin", "los", "In", "drei", "gehen",
       "Ein", "wird", "So", "La", "wir", "Eine", "Das", "Wir", "allen", "Geri",
       "nun", "sind", "ins", "nun", "auch", "+++", "+++:", "einen", "fahren",
       "nicht", "noch", "ohne", "seit", "letzte", "neu", "Drei", "Unter", "Wochen",
       "Diese", "diese", "Auf", "Wo", "Sie", "immer", "einer", "bring", "erste",
       "Neue", "of", "m", "Aus", "nach", "fuer", "ueber", "T", "frei", "macht",
       "UeBERSICHT", "unter", "per", "cu", "das", "will", "Ueber", "alte", "keine",
       "man", "wie", "Zwei","zwei", "alle", "hol", "eins", "Wie", "Nach", "holt",
       "weiter", "Vor", "weg", "Was", "De", "Un", "mein", "Deutschland", "nehmen",
       "Internet:", "gar", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Sport",
       "nie", "lag", " ", "hat", "18", "hat", "mehr", "Mehr", "soll", "All", "durch",
       "kommt", "zurueck", "halt", "erst", "acht", "aller", "raus", "Keine", 
       "beste", "Ukraine-", "geben", "geben", "machen", "Tuer", "fest",
       "wegen", "dir", "20", "is", "Fußball", "gut", "it", "No", "no", "gegen",
       "US", "An", "sein", "&", "Zu", "da", "sie", "uns", "mit", "Mit", "kann", 
       "mit", "New", "dies", "geht", "Auto", "neue", "aufs", "oder", "Bei", 
       "echte", "Wind", "werde", "Tage", "C", "je", "2014","14", "reist", "werden", 
       "Meter", "meist", "Wenn", "habe", "Groß", "wieder", "stand", "große",
       "Jahr", "heim", "weit", "deutsche", "Frau", "Zeit", "Familie", "Liebe",
       "beim", "Erst", "Komm", "eines", "ihre", "Haus", "\"Ich", "Mann", "kommen",
       "teil", "Fuß", "teilt", "eure", "hart", "Welt", "Fuss", "mach", "eben",
       "neuen", "Hand", "Warum", "Alle", "lange", "seine", "koennte", "gemein",
       "zweites", "alten", "sucht", "\"Die", "vier", "fuenf", "voll", "andere",
       "einem", "muessen", "Klaus", "statt", "Will", "fort", "fort", "gleich",
       "wollen", "aber", "neuer", "Ende", "muessen", "bringt", "statt", "setzt",
       "enden", "viel", "Ende", "plant", "bringt", "Nachrichten", "droht", 
       "Arme", "statt", "setzt", "ganz", "Deutsch", "gebe", "eher", "steht",
       "sehen", "gehe", "eher", "sieht", "\"Das", "jede", "denken", "stark",
       "Berlin", "Deutsche", "Bund", "Taxi"]

exception = ["EU", "Eu", "USA", "US", "BND", "IS", "Tod", "CIA", "NSA", "ARD", "ZDF",
	   		 "Uni", "UNI", "UNO", "CDU", "CSU", "SPD", "AFD", "Afd", "FDP", "Uno", "BMW",
	   		 "PKK"]
