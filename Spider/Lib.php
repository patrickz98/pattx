<?php

function splitArray($array, $split)
{
    $arrayCount = count($array);
    $newArray   = array();

    $level = 0;
    $main  = 0;
    $newArray[ $main ] = array();

    for ($id = 0; $id < $arrayCount; $id++)
    {
        array_push($newArray[ $main ], $array[ $id ]);

        if ($id == $split)
        {
            $level += $split;
            $main  += 1;

            $newArray[ $main ] = array();
        }
    }

    return $newArray;
}

function joinArray($array)
{
    $newArray = array();

    for ($inx = 0; $inx < count($array); $inx++)
    {
        foreach ($array[ $inx ] as $key => $value)
        {
            array_push($newArray, $value);
        }
    }

    return $newArray;
}

function deMoroniseBody($body)
{
    $body = str_replace(". ", " ", $body);
    $body = str_replace(".",  "",  $body);
    $body = str_replace(",",  "",  $body);
    $body = str_replace("\"", "",  $body);
    $body = str_replace("’",  "'", $body);
    $body = str_replace("'",  "",  $body);
    $body = str_replace("“",  "",  $body);
    $body = str_replace("”",  "",  $body);
    $body = str_replace(":",  "",  $body);
    $body = str_replace(";",  "",  $body);
    $body = str_replace("(",  "",  $body);
    $body = str_replace(")",  "",  $body);
    $body = str_replace("[",  "",  $body);
    $body = str_replace("]",  "",  $body);
    $body = str_replace("@",  "",  $body);
    $body = str_replace("|",  "",  $body);
    $body = str_replace("/",  "",  $body);
    $body = str_replace("\\", "",  $body);
    $body = str_replace("#",  "",  $body);
    $body = str_replace("?",  "",  $body);
    $body = str_replace("!",  "",  $body);

    return $body;
}

function deMoroniseHtmlForPage($content)
{
    $breaklineID = "###";
    $imgID       = "!!";

    $content = preg_replace("/<img *src=\"(.*?)\".*?>/", "<img>$imgID$1$imgID</img>", $content);

    $content = str_replace("</p>", $breaklineID, $content);
    $content = str_replace("<br>", $breaklineID, $content);
    $content = str_replace("\n",   $breaklineID, $content);

    $result = deMoroniseHtml($content);

    $result = preg_replace("/( {1,})/", " ", $result);
    $result = preg_replace("/(($breaklineID ){1,}$breaklineID)/", $breaklineID, $result);

    $result = str_replace($breaklineID, " " . $breaklineID . " ", $result);
    $result = preg_replace("/ {1,}($breaklineID) {1,}/", " $breaklineID ", $result);

    // Kommas
    $result = preg_replace("/ \,/", ",", $result);
    $result = preg_replace("/ \./", ".", $result);

    return $result;
}

function deMoroniseHtml($content)
{
    if (strpos($content, ">") === false) return $content;

    $content = str_replace("\n", "", $content);
    $content = preg_replace("/(<.*?>)/", "", $content);

    return $content;
}

function removeHtmlSuffix($path)
{
    $dirPath = explode("/", $path);
    // remove /.*?.html
    unset($dirPath[ count($dirPath) - 1 ]);

    return join("/", $dirPath);
}

function writeFileDir($dir, $destination, $content)
{
    $destination = $dir . $destination;

    @mkdir($dir, 0777, true);

    writeFile($destination, $content);
}

function writeFile($destination, $content)
{
    if ($content == null) return;

//     echo "--> $destination\n";

    $myfile = @fopen($destination, "w");
    @fwrite($myfile, $content);
    @fclose($myfile);
}

function readJson($file)
{
    $myfile = file_get_contents($file);
    $json   = json_decode($myfile, true);

    return $json;
}

function addJson($json, $data)
{
    $file     = @file_get_contents($json);
    $jsonData = json_decode($file, true);

    if ($file == null)
    {
        $jsonData = array();
    }

    if (in_array($data, $jsonData)) return false;

    array_push($jsonData, $data);

    sort($jsonData);

    $myfile = @fopen($json, "w");
    @fwrite($myfile, json_encode($jsonData, JSON_PRETTY_PRINT));
    @fclose($myfile);

    return true;
}

function niceJson($json)
{
    $json = json_decode($json, true);
    $json = prettyJson($json);

    return $json;
}

function prettyJson($json)
{
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
