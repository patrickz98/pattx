<?php

include("../../Spider/Lib.php");
include("../../Spider/Elastic.php");

function getByUuid($server, $index, $type, $uuid)
{
    $hits = array();
    $json = json_decode(getDataByUuid($server, $index, $type, $uuid), true);

    foreach ($json[ "hits" ][ "hits" ] as $key => $value)
    {
        $hit = $value[ "_source" ];
        $hit[ "id" ] = $value[ "_id" ];

        array_push($hits, $hit);
    }

    return prettyJson($hits);
}

function getById($server, $index, $type, $id)
{
    $json = json_decode(getDataById($server, $index, $type, $id), true);
    $json = $json[ "_source" ];
    $json[ "id" ] = $id;
    return prettyJson($json);
}

function postByUuid($server, $index, $type, $uuid, $json)
{
    $json = json_decode($json, true);
    $json[ "uuid" ] = $uuid;
    $json = json_encode($json);

    $response = postData($json, $server, $index, $type);
    $response = json_decode($response, true);

    return $response[ "_id" ];
}

function updateById($server, $index, $type, $id, $json)
{
    $json = json_decode($json, true);

    $json = json_encode($json);
    echo $json;
    putData($json, $server, $index, $type, $id);
}

function deleteById($server, $index, $type, $id)
{
    $result = deleteDataById($server, $index, $type, $id);
    return niceJson($result);
}

?>
