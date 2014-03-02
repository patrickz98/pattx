#!/bin/bash

ssh -l odroid 192.168.0.11 "php boom.php &"
read pid-U3-1

ssh -l odroid 192.168.0.11 "php boom.php &"
read pid-U3-2

ssh -l pi 192.168.0.25 "php boom.php &"
read pid-pi

echo $pid-pi \n
echo $pid-U3-1 \n
echo $pid-U3-2 \n

