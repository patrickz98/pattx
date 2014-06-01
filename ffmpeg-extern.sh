#!/bin/bash

pwd
read pwd
echo $pwd
pwd = $pwd + $1

sudo ln -s pwd/$1 /var/www/
ssh patty@debian.local "ffmpeg -i www/$1 $2"

