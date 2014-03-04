#!/usr/bin/php
<?php

while(true)
{

$ip = "192.168.0.19";

$online = exec("ping $ip -c 1 |grep received");

if($online == "1 packets transmitted, 1 received, 0% packet loss, time 0ms");
	{
	echo "$ip ist online \n";
	}
	else
	{
        echo "$ip ist off \n";
        }

}
?>
