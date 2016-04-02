<?php

function writeFileDir($dir, $destination, $content)
{
    $destination = $dir . $destination;

    @mkdir($dir, 0777, true);

    writeFile($destination, $content);
}

function writeFile($destination, $content)
{
    if ($content == null) return;

    echo "--> $destination\n";

    $myfile = @fopen("$destination", "w");
    @fwrite($myfile, $content);
    @fclose($myfile);
}

function niceJson($json)
{
    $json = json_decode($json, true);
    $json = json_encode($json, JSON_PRETTY_PRINT);

    return $json;
}

function getJson($url)
{
    $urlJson = file_get_contents($url);
    $urlJson = niceJson($urlJson);

    writeFile("out", $urlJson);
}

?>
