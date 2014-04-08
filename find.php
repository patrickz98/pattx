<?php

exec("find /media/iVideo/Videos/Series-1/ -name '*.vob' -size +750000k |grep -E .vob > /var/www/xxx.txt");
$i = 1;
$zeilen = exec("cat /var/www/xxx.txt |wc -l");

while($i < $zeilen)
{
	$txt = file('xxx.txt');
	exec("touch /var/www/jobs/$i.txt");
	echo $txt[$i];

	$inhalt = $txt[$i];
        $handle = fopen ("/var/www/jobs/$i.txt", "a");
        fwrite ($handle,"".$inhalt."\r\n");
        fclose ($handle);

	$i++;
}


?>
