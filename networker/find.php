#!/usr/bin/php
<?php

include 'find.conf';
exec("find $id -name '*.vob' -size +750000k |grep -E .vob > /var/www/xxx.txt");
exec("rm /var/www/jobs/*");
$i = 1;
$zeilen = exec("cat /var/www/xxx.txt |wc -l");


$done = exec("curl http://odroid-u4.local/done.txt| grep media > done-1.txt");

exec("cat done-1.txt > done-cache.txt");
exec("sed '/^\s*$/d' done-cache.txt > done-master.txt");
exec("rm done-1.txt done-cache.txt");
exec("mv done-master.txt /var/www/");


while($i < $zeilen)
{
	$txt = file('/var/www/xxx.txt');
	exec("touch /var/www/jobs/$i.txt");
	echo $txt[$i];

	$inhalt = $txt[$i];
        $handle = fopen ("/var/www/jobs/$i.txt", "a");
        fwrite ($handle,"".$inhalt."\r\n");
        fclose ($handle);

	$i++;

}


?>
