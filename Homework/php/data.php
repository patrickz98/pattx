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
//

$action = $_GET[ "action" ];
$type   = $_GET[ "type"   ];
$uuid   = $_GET[ "uuid"   ];
$id     = $_GET[ "id"     ];
$json   = $_GET[ "json"   ];

if ($action == null) exit(0);
if ($type   == null) exit(0);

// http://patrick-macbook.local/homework/data.php?action=g&type=teacher&id=AVTIlMRbYnkdd7Ja7TUV
if (($action == "g") && ($id != null))
{
    echo getById($server, $index, $type, $id);
    exit(0);
}

// http://patrick-macbook.local/homework/data.php?action=f&type=teacher&uuid=PATpLAJgPkDt6iI38jVw
if (($action == "f"))
{
    echo getByUuid($server, $index, $type, $uuid);
    exit(0);
}

// http://patrick-macbook.local/homework/data.php?action=p&type=teacher&uuid=PATpLAJgPkDt6iI38jVw&json=%7B%22Name%22%3A%20%22Mr.%20Zolu%22%2C%20%22ShortName%22%3A%20%22Zo%22%2C%20%22Subjects%22%3A%20%22Space%22%2C%20%22Notes%22%3A%20%22Cool%22%2C%20%22School%22%3A%20%22GSH%22%7D
if (($action == "p") && ($json != null))
{
    postByUuid($server, $index, $type, $uuid, $json);
    exit(0);
}

// http://patrick-macbook.local/homework/data.php?action=u&type=teacher&uuid=PATpLAJgPkDt6iI38jVw&id=AVTLAnFkBE-ZAybXntx3&json=%7B%22Name%22%3A%20%22Mr.%20Boom%22%2C%20%22ShortName%22%3A%20%22Bo%22%2C%20%22Subjects%22%3A%20%22PGW%22%2C%20%22Notes%22%3A%20%22%22%2C%20%22School%22%3A%20%22AvH%22%7D
if (($action == "u") && ($json != null) && ($id != null))
{
    updateById($server, $index, $type, $id, $json);
}

?>
