#!/usr/bin/php
<?php

$id = "http://odroid-u3.local";
$jobs = "/jobs/";
$a = 1;
$b = ".txt";
$c = exec("curl '$id'/xxx.txt| wc -l");
$ziel = "cache/";
$out = "out";
$format = ".mp4";
$done = exec("curl '$id'/done.txt| grep media");

while($a < $c)
{
	$dat = exec("curl $id$jobs$a$b| grep media");

	echo "ffmpeg -i $id$dat $ziel$out$a$format\n";
	$a++;
}

?>
