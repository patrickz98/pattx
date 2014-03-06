#!/usr/bin/php
<?php

$a = 0;

while($a < 254)
{

$a++;

#if ($a == 254);
#    {
#    $a = 1;
#    }

$ip = "192.168.0.$a";

$online = exec("ping $ip -c 1 |grep received");

$time = date("H:i");
$date = date("d-m-Y");


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

	$inhalt = "$ip ist offline um $time";
        $handle = fopen ("off/$date.txt", "a");
        fwrite ($handle," ".$inhalt."\r\n");
        fclose ($handle);

	}

#sleep(60);
}
?>
