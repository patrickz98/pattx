<?php

function writeFile($file, $data)
{
    $myfile = @fopen($file, "w");
    @fwrite($myfile, $data);
    @fclose($myfile);
}

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

function getLocation($content)
{
    preg_match_all("/\|Latitude = (.*)/",  $content, $latitude,  PREG_PATTERN_ORDER);
    preg_match_all("/\|Longitude = (.*)/", $content, $longitude, PREG_PATTERN_ORDER);

    $location = array();
    $location[ "latitude" ]  = $latitude[ 1 ][ 0 ];
    $location[ "longitude" ] = $longitude[ 1 ][ 0 ];

    return $location;
}

function getFiles($links)
{
    $files = array();

    foreach ($links as $key => $value)
    {
        preg_match_all("/File:(.*)/", $value, $match, PREG_PATTERN_ORDER);
        if ($match[ 0 ])
        {
            array_push($files, $match[ 0 ][ 0 ]);
        }
    }

    return $files;
}

function getLinks($content)
{
    // preg_match_all("/\[\[(.*?[\[\]].*?)\]\]/", $content, $match, PREG_PATTERN_ORDER);
    preg_match_all("/\[\[(.*?)\]\]/", $content, $match, PREG_PATTERN_ORDER);
    $match = $match[ 1 ];

    foreach ($match as $key => $value)
    {
        preg_match_all("/(.*?)\|.*/", $value, $filter, PREG_PATTERN_ORDER);

        if ($filter[ 1 ])
        {
            $match[ $key ] = str_replace(" ", "_", $filter[ 1 ][ 0 ]);
        }
        else
        {
            $match[ $key ] = str_replace(" ", "_", $value);
        }
    }

    return $match;
}

function getLinksRaw($title)
{
    echo "--> $title\n";

    $resultJson = array();

    $wiki = "https://en.wikipedia.org/w/api.php?action=query&titles=";

    $wikiJson = file_get_contents($wiki . $title . "&prop=revisions&rvprop=content&format=json");
    $wikiJson = json_decode($wikiJson, true);
    $content = $wikiJson[ "query" ][ "pages" ];

    if (count($content) == 0) return;

    foreach ($content as $key => $value)
    {
        $content  = $value[ "revisions" ][ 0 ][ "*" ];
        $links    = getLinks($content);

        if (count($links) == 0) continue;

        array_push($resultJson, $links);
    }

    return joinArray($resultJson);
}

function getWikiJson($title)
{
    $resultJson = array();

    $wiki = "https://en.wikipedia.org";

    $structure = "./JSON/";
    $wikiJson = file_get_contents($wiki . "/w/api.php?action=query&titles=". $title . "&prop=revisions&rvprop=content&format=json");
    $wikiJson = json_decode($wikiJson, true);

    // $content = $wikiJson[ "query" ][ "pages" ][ "6097297" ][ "revisions" ][ 0 ][ "*" ];
    $content = $wikiJson[ "query" ][ "pages" ];

    if (count($content) == 0) return;

    foreach ($content as $key => $value)
    {
        $title = $value[ "title" ];
        $title = str_replace(" ", "_", $title);

        $revisions = count($value[ "revisions" ]);

        $resultJson[ $title ] = array();

        $resultJson[ $title ][ "title" ] = $title;
        $resultJson[ $title ][ "wiki"  ] = $wiki . "/wiki/" . $title;
        $resultJson[ $title ][ "key"   ] = $key;

        echo "--> " . $title . "\n";

        if ($revisions > 1)
        {
            echo "revisions: $revisions\n";
            echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n";
            exit(0);
        }

        $content  = $value[ "revisions" ][ 0 ][ "*" ];
        $links    = getLinks($content);

        if (count($links) == 0) continue;

        $location = getLocation($content);
        $resultJson[ $title ][ "latitude"  ] = $location[ "latitude" ];
        $resultJson[ $title ][ "longitude" ] = $location[ "longitude" ];

        if ($location[ "latitude" ] && $location[ "longitude" ])
        {
            echo "++> location\n";
        }

        // $files = getFiles($links);
        // $resultJson[ $title ][ "files" ] = $files;

        $resultJson[ $title ][ "linksCount" ] = count($links);
        $resultJson[ $title ][ "links" ]      = $links;

        @mkdir($structure, 0777, true);

        $destiantion = $structure . str_replace("/", "_", $title);
        $myfile = @fopen($destiantion . ".json", "w");
        @fwrite($myfile, json_encode($resultJson[ $title ], JSON_PRETTY_PRINT));
        @fclose($myfile);

        // @mkdir("./TXT/", 0777, true);
        // $destiantion = "./TXT/" . str_replace("/", "_", $title);
        // $myfile = @fopen($destiantion . ".txt", "w");
        // @fwrite($myfile, $content);
        // @fclose($myfile);
    }

    return $resultJson;
}

function nodes($json)
{
    $json   = array_unique($json);
    $json   = array_values($json);

    $result = array();
    $nodes  = array();

    foreach ($json as $key => $value)
    {
        $pushJSON = array();
        $pushJSON[ "id"    ] = $key;
        $pushJSON[ "label" ] = $value;

        array_push($nodes, $value);
        array_push($result, $pushJSON);
    }

    writeFile("nodes.json", json_encode($result, JSON_PRETTY_PRINT));

    return $nodes;
}

function edges($json, $nodes)
{
    $result = array();

    foreach ($json as $key => $value)
    {
        foreach ($value as $key2 => $link)
        {
            $from = array_search($key,  $nodes);
            $to   = array_search($link, $nodes);

            if ($from == $to) continue;

            $pushJSON = array();
            $pushJSON[ "from" ] = $from;
            $pushJSON[ "to"   ] = $to;

            array_push($result, $pushJSON);
        }
    }

    writeFile("edges.json", json_encode($result, JSON_PRETTY_PRINT));
}

$links = array();

$Risk_society = getLinksRaw("Production_(economics)");
array_push($Risk_society, "Production_(economics)");

$Ulrich_Beck = getLinksRaw("Industry");
array_push($Risk_society, "Industry");

array_push($links, $Ulrich_Beck, $Risk_society);

$links = joinArray($links);
$links = array_unique($links);
$links = array_values($links);

$nodes = nodes($links);

$tmp = array();
$tmp[ "Production_(economics)" ] = $Risk_society;
$tmp[ "Industry" ]  = $Ulrich_Beck;

edges($tmp, $nodes);

// $cloud = array();
//
// foreach ($links as $key => $link)
// {
//     $cloud[ $link ] = array_unique(getLinksRaw($link));
// }
//
// error_log(json_encode($cloud, JSON_PRETTY_PRINT));

?>
