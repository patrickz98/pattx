<?php

function getJson($title)
{
    $url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=de&tl=en&dt=t&q=";

    $urlJson = file_get_contents($url . $title);

    echo $urlJson;

    $urlJson = json_decode($urlJson, true);
    $urlJson = json_encode($urlJson, JSON_PRETTY_PRINT);

    $myfile = @fopen($title . ".json", "w");
    @fwrite($myfile, $urlJson);
    @fclose($myfile);
}

getJson($argv[ 1 ]);
?>
