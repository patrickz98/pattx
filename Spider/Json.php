<?php

function getJson($url, $file)
{
    $urlJson = file_get_contents($url);
    $urlJson = json_decode($urlJson, true);
    $urlJson = json_encode($urlJson, JSON_PRETTY_PRINT);


    $myfile = @fopen($file, "w");
    @fwrite($myfile, $urlJson);
    @fclose($myfile);
}

getJson($argv[ 1 ], $argv[ 2 ]);
?>
