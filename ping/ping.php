#!/usr/bin/php
<?php

while(true)
{

$ip = "192.168.0.1";

$online = exec("ping $ip -c 1 |grep received");

if ($online == "1 packets transmitted, 1 received, 0% packet loss, time 0ms")
	{
	echo "$ip ist online \n";

	$date = date("d.m.Y H:i");
        $inhalt = "$ip ist online um $date";
        $handle = fopen ("log.txt", "a");
        fwrite ($handle," ".$inhalt."\r\n");
        fclose ($handle);

	}
else
	{
        echo "$ip ist nicht online \n";
        }

sleep(10);
}
?>
