#!/usr/bin/php
<?php


$ip = "192.168.0.1";

$online=exec("ping $ip -n 1");

if($online=="Zeitueberschreitung der Anforderung");
{
print "$ip ist offline";
}
if($online!=="Zeitueberschreitung der Anforderung");
{
print "$ip ist online";
}



?>
