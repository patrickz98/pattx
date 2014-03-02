<?php

while(true)
{

$file = fopen ("http://rguhr.de/", "r");
if (!$file)
    {
    echo "Unable to open remote file.\n";
    exit;
    }
    else
    {
    echo "blablabal \n";
    }

#sleep(1);
}

?>
