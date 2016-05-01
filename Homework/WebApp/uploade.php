<?php

include("../Lib.php");
include("../Elastic.php");

header("Content-Type: text/plain");

$json = $_GET[ "json" ];

$server = "localhost";
$index  = "homework";
$type   = "test";

postData($json, $server, $index, $type);

// echo urlencode($json);
echo niceJson($json);

?>
