<?php

function Ping($host, $timeout = 100, $quiet = false)
{
	$time = -1;
	//
    // Create the socket, the last '1' denotes ICMP
    //

	$socket = @socket_create(AF_INET, SOCK_RAW, 1);

    if ($socket === false)
    {
    	echo "Use SUUUUUUUUDOOOOOOOO Spacko...\n";
    	exit(0);
    }

	$sec  = floor($timeout / 1000);
	$usec = ($timeout % 1000) * 1000;

	socket_set_option($socket, SOL_SOCKET, SO_RCVTIMEO, array("sec" => $sec, "usec" => $usec));

	if (@socket_connect($socket, $host, null) === false)
	{
		if (! $quiet) echo "Cannot resolve '$host'.\n";
	}
	else
	{
		list($start_usec,$start_sec) = explode(" ",microtime());
		$start_time = ((float) $start_usec + (float) $start_sec);
		$package = "\x08\x00\x19\x2f\x00\x00\x00\x00\x70\x69\x6e\x67";
		socket_send($socket,$package,strlen($package),0);
		if (@socket_read($socket,255))
		{
			list($end_usec,$end_sec) = explode(" ",microtime());
			$end_time = ((float) $end_usec + (float) $end_sec);
			$total_time = $end_time - $start_time;
			$time = floor($total_time * 1000);
			if ($time <= 1) $time = -1;
		}
	}

	socket_close($socket);

	return $time;
}

function ping_port($host, $port)
{
    // $port = 80;
    $waitTimeoutInSeconds = 0.1;

    $fp = @fsockopen($host,$port,$errCode,$errStr,$waitTimeoutInSeconds);

    if ($fp)
    {
        return true;
    }
    else
    {
        return false;
    }
}
// $servers = array();

for ($ina = 31; $ina < 255; $ina++)
{
    for ($inb = 16; $inb < 255; $inb++)
    {
        for ($inc = 214; $inc < 255; $inc++)
        {
            for ($ine = 100; $ine < 255; $ine++)
            {
                $host = "$ina.$inb.$inc.$ine";
                // $host = "31.16.214.133";
                // $ping = ping($ip);
                $ping = Ping($host);

				// echo "$host\n";

                if ($ping > -1)
                {
                    if (ping_port($host, 9981)) echo "$host:9981\n";
                    if (ping_port($host, 6868)) echo "$host:6868\n";
                    // $servers[ $ip ] = $ping;
                }
            }
        }
    }
}

echo "Done.\n";
// echo json_encode($servers, JSON_PRETTY_PRINT) . "\n";

?>
