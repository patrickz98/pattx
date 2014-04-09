#!/usr/bin/php
<?php

$pings = 1;

function ping($pings)
{
	$address = "$pings";
	echo "pings";
	$pings++;
}

ping();

?>
