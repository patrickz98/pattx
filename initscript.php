<?php

$var1 = exec('ps ax | grep "noip"| wc -l');

	if ( $var1 == 2 )
        {
                exec('sudo noip2');
        }





# $log = fopen ("../log/initscript.log", "a+");
# fwrite ($log, date ("d.m.Y H:i:s ") .getmypid()." starte gerade\n" );
# fclose ($log);

#while (true)
#{
#	$log = fopen ("../log/initscript.log", "a+");
#	fwrite ($log, date ("d.m.Y H:i:s ").getmypid()." bin am leben\n" );
#	fclose ($log);
#	sleep (5);
#}





?>
