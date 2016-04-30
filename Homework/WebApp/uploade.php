<?php

include("../Lib.php");
include("../Elastic.php");

header("Content-Type: text/plain");

$json = $_GET[ "json" ];
// $json = '{"Country":"de","School":"GSH","Grade":"S2","CreateDate":1462038618260,"Subject":"English","Course":null,"Teacher":null,"DestinyDate":"A102","Room":"A102","Task":"Culture","Notes":null,"EstimatedTime":null,"Priority":"middel"}';

$server = "localhost";
$index  = "homework";
$type   = "test";

postData($json, $server, $index, $type);

// echo urlencode($json);
echo niceJson($json);

?>
