<?php

//
// find Article -name "*.json" -exec php Extract.php {} \;
//

include("../Elastic.php");

$inFile = $argv[ 1 ];

echo "--> $inFile\n";

$json = file_get_contents($inFile);

$server = "localhost";
$index  = "guardian";
$type   = "article";

putData($json, $server, $index, $type);

?>
