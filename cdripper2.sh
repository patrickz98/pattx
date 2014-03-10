
#!/bin/sh
#/usr/bin/mplayer -dvd-device /dev/sr0 dvdnav://$1 -dumpstream -dumpfile ./ripped_$1.vob
/usr/local/bin/mplayer -dvd-device /dev/sr0 dvdnav://$1 -dumpstream -dumpfile ./ripped_$1.vob

echo "scp ripped_$1.vob odroid@odroid-X2.local:/media/iPtarick/DVD"

scp ripped_$1.vob odroid@odroid-X2.local:/media/iPtarick/DVD

echo "rm ripped_$1.vob"

rm ripped_$1.vob
