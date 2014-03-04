<?php

//$var3 = exec('php -f tvstart.php &');
//exec('php -f tvstart.php &');
//echo "$var3";

while(true) {


	
	$var1 = exec('ps ax | grep "tvheadend" | wc -l');
	$var2 = exec('cat log.txt | wc -l');
	
	if ( $var1 >= 3 )
	{
		//echo "Tvheadend Work \n"; 
	}
	
	if ( $var1 == 2 )
	{
		exec('sudo service tvheadend start');
		//echo "Tvheadend must be restarted \n";
	
		$inhalt = exec('uptime');
		$date = exec('date');
		$handle = fopen ("log.txt", "a");
		#fwrite ($handle," ".$inhalt."\r\n");
		fwrite ($handle," ".$date."\r\n");
		fclose ($handle);
		
	}
	
sleep(100);
	
	
}	




?>
