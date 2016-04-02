<?php

function getJson($title)
{
    $url = "http://api.urbandictionary.com/v0/define?term=";

    $urlJson = file_get_contents($url . $title);
    $urlJson = json_decode($urlJson, true);
    $urlJson = json_encode($urlJson, JSON_PRETTY_PRINT);


    $myfile = @fopen($title . ".json", "w");
    @fwrite($myfile, $urlJson);
    @fclose($myfile);
}

getJson($argv[ 1 ]);
?>
