<?php
include("../../Lib.php");
include("../../Pons/pons-include.php");

header("Content-Type: text/plain");

$trans = ponsJson($_GET[ "q" ], false);

echo prettyJson($trans);

?>
