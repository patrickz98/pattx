
#!/bin/sh
#/usr/bin/mplayer -dvd-device /dev/sr0 dvdnav://$1 -dumpstream -dumpfile ./ripped_$1.vob
#/usr/local/bin/mplayer -dvd-device /dev/sr0 dvdnav://$1 -dumpstream -dumpfile ./ripped_$1.vob
/opt/local/bin/mplayer -dvd-device /dev/disk1 dvdnav://$1 -dumpstream -dumpfile ./ripped_$1.vob

