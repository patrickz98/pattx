#!/usr/bin/php
<?php


$id = "http://odroid-u3.local";
$jobs = "/jobs/";
$a = 1;
$b = ".txt";
$c = exec("curl '$id'/xxx.txt| wc -l");
$d = 0;
$ziel = "cache/";
$out = "out";
$format = ".mp4";

exec("curl '$id'/done.txt| grep media > done.txt");
$done = file("done.txt");
$donewc = exec("cat done.txt| wc -l");


while($a < $c)
{

	$dat = exec("curl $id$jobs$a$b| grep media");

	while($d < $donewc)
	{
		if($done[$d] = $dat)
		{
			echo $done[$d];
			$a++;
			return;
		}
		$d++;
	}


	echo "ffmpeg -i $id$dat $ziel$out$a$format\n";
	//exec("ffmpeg -i $id$dat $ziel$out$a$format");
	$a++;
}

?>
