#!/usr/bin/php
<?php

$id = "http://odroid-u3.local";
$jobs = "/jobs/";
$a = 0;
$b = ".txt";
$c = exec("curl '$id'/xxx.txt| wc -l");
$d = 0;
$ziel = "cache/";
$out = "out";
$format = ".mp4";

exec("curl '$id'/done-master.txt| grep media > finish.txt");
$done = file("finish.txt");
$donewc = exec("cat finish.txt| wc -l");


while($a < $c)
{

	$dat = exec("curl $id$jobs$a$b| grep media");

	while($d < $donewc)
	{
		if($done[$d] == $dat)
		{
			echo $done[$d];
			$a++;
			return;
		}
		$d++;
	}


	echo "ffmpeg -i $id$dat $ziel$out$a$format\n";
	//exec("ffmpeg -i $id$dat $ziel$out$a$format");

	$inhalt = "$dat";
        $handle = fopen ("done.txt", "a");
        fwrite ($handle,"".$inhalt."\r\n");
        fclose ($handle);
	//exec("sed '/^\s*$/d' done.txt > done.txt");

	$a++;
}

?>
