<?php

include("../php/interface.php");

header("Content-Type: text/plain");

$server = "localhost";
$index  = "homework";

//
// action
// g --> get
// f --> find
// p --> post (New)
// u --> update
// d --> delete
//

// $endPoint = $_GET[ "endPoint" ];
// $action   = $_GET[ "action"   ];
// $type     = $_GET[ "type"     ];
// $uuid     = $_GET[ "uuid"     ];
// $id       = $_GET[ "id"       ];
// $json     = $_GET[ "json"     ];
//
// if ($action == null) exit(0);
// if ($type   == null) exit(0);
//
// // http://patrick-macbook.local/homework/data.php?action=g&type=teacher&id=AVTSxfCrcnoLerTG9yfI
// if (($action == "g") && ($id != null))
// {
//     echo $endPoint . "(" . getById($server, $index, $type, $id) . ");\n";
//     exit(0);
// }
//
// // http://patrick-macbook.local/homework/data.php?action=f&type=teacher&uuid=PATpLAJgPkDt6iI38jVw
// if (($action == "f"))
// {
//     echo $endPoint . "(" . getByUuid($server, $index, $type, $uuid) . ");\n";
//     exit(0);
// }
//
// // http://patrick-macbook.local/homework/data.php?action=p&type=teacher&uuid=PATpLAJgPkDt6iI38jVw&json=%7B%22Name%22%3A%20%22Mr.%20Zolu%22%2C%20%22ShortName%22%3A%20%22Zo%22%2C%20%22Subjects%22%3A%20%22Space%22%2C%20%22Notes%22%3A%20%22Cool%22%2C%20%22School%22%3A%20%22GSH%22%7D
// if (($action == "p") && ($json != null))
// {
//     echo $endPoint . "(\"" . postByUuid($server, $index, $type, $uuid, $json) . "\");\n";
//     exit(0);
// }
//
// // http://patrick-macbook.local/homework/data.php?action=u&type=teacher&uuid=PATpLAJgPkDt6iI38jVw&id=AVTLAnFkBE-ZAybXntx3&json=%7B%22Name%22%3A%20%22Mr.%20Boom%22%2C%20%22ShortName%22%3A%20%22Bo%22%2C%20%22Subjects%22%3A%20%22PGW%22%2C%20%22Notes%22%3A%20%22%22%2C%20%22School%22%3A%20%22AvH%22%7D
// if (($action == "u") && ($json != null) && ($id != null))
// {
//     updateById($server, $index, $type, $id, $json);
// }
//
// // http://patrick-macbook.local/homework/data.php?action=d&type=teacher&id=AVTSxfCrcnoLerTG9yfI
// if (($action == "d") && ($id != null))
// {
//     echo "Delete\n";
//     echo $endPoint . "(\"" . deleteById($server, $index, $type, $id) . "\");\n";
// }

echo deleteById($server, $index, "teacher", "AVTSxfCrcnoLerTG9yfI");
// echo getDataById($server, $index, "teacher", "AVTSxfCrcnoLerTG9yfI");

?>
