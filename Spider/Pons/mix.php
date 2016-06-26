<?php

include("../Lib.php");

$list = readJson("./Word-list.json");
shuffle($list);

echo prettyJson($list) . "\n";
?>
