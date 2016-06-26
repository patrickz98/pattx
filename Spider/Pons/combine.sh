#!/bin/sh

# ffmpeg -f concat -i < (for f in Audio/*.mp3; do echo "file '$PWD/$f'"; done) -c copy output.mp3
# grep -R Error Audio/
rm -f mylist.txt;
for i in Audio/*.mp3; do printf "file '$i'\n" >> mylist.txt; done

ffmpeg -f concat -i mylist.txt -c copy $1.mp3;
ffmpeg -i $1.mp3 $1;
rm -f $1.mp3;
rm -f mylist.txt;
