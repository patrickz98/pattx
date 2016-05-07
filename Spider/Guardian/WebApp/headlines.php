<?php

include("../../Lib.php");

header("Content-Type: text/plain");

$article = readJson("../Article-list.json");

echo prettyJson($article);

?>
