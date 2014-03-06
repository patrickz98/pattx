#!/usr/bin/php
<?php

while(true)
{

$ip = "192.168.0.1";

$online = exec("ping $ip -c 1 |grep received");

$time = date("H:i");
$date = date("d-m-Y");

#$file-on =/on"
#$file-off

if ($online == "1 packets transmitted, 1 received, 0% packet loss, time 0ms")
	{
	echo "$ip ist online \n";

        $inhalt = "$ip ist online um $time";
        $handle = fopen ("on/$date.txt", "a");
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
