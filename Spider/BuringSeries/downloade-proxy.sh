#!/bin/sh

youtube-dl --proxy "patrick-odroid.local:8118" $1 -o $2.mp4
