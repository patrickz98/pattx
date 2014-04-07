#!/bin/sh

id="http://odroid-u3.local/"
dat="Quentin-Tarantino/From-Dusk-Till-Dawn/Disk-1/vts_01_1.vob"
out="From-Dusk-Till-Dawn.mp4"

ffmpeg -i $id$dat $out

