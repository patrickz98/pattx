#!/usr/bin/php
<?php

while(true)
{

$ip = "192.168.0.4";

$online = exec("ping $ip -c 1 |grep received");

$time = date("H:i");
$date = date("d-m-Y");


if ($online == "1 packets transmitted, 1 received, 0% packet loss, time 0ms")
	{
	#echo "$ip ist online \n";

        $inhalt = "Lukas ist online am $date um $time";
        $handle = fopen ("on/lukas.txt", "a");
        fwrite ($handle," ".$inhalt."\r\n");
        fclose ($handle);

	}
else
	{
        #echo "$ip ist nicht online \n";

	$inhalt = "Lukas ist offline am $date um $time";
        $handle = fopen ("off/lukas.txt", "a");
        fwrite ($handle," ".$inhalt."\r\n");
        fclose ($handle);

	}

sleep(600);
}
?>
