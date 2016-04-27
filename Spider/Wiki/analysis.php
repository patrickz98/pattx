<?php

include("../Lib.php");
include("../Elastic.php");

function getLocation($content)
{
    // coordinates = {{Coord|40.666|-73.966|
    preg_match_all("/coordinates = \{\{Coord\|(.*?)\|(.*?)\|/",  $content, $coordinates,  PREG_PATTERN_ORDER);

    //
    // latitude  = lat
    // longitude = lon
    //

    $location = array();
    $latitude  = $coordinates[ 1 ][ 0 ];
    $longitude = $coordinates[ 2 ][ 0 ];


    if ($latitude && $longitude)
    {
        $location[ "lat" ] = floatval($latitude);
        $location[ "lon" ] = floatval($longitude);

        return $location;
    }

    // preg_match_all("/\| latd = ([0-9]+)(\.[0-9]+)?/",  $content, $latitude,  PREG_PATTERN_ORDER);
    // preg_match_all("/\| longd = ([0-9]+)(\.[0-9]+)?/", $content, $longitude, PREG_PATTERN_ORDER);
    preg_match_all("/latd = ([0-9]+)(\.[0-9]+)?/",  $content, $latitude,  PREG_PATTERN_ORDER);
    preg_match_all("/longd = ([0-9]+)(\.[0-9]+)?/", $content, $longitude, PREG_PATTERN_ORDER);

    $location = array();

    if ($latitude[ 1 ][ 0 ] && $latitude[ 1 ][ 0 ])
    {
        $location[ "lat" ] = floatval($latitude[ 1 ][ 0 ]);
        $location[ "lon" ] = floatval($longitude[ 1 ][ 0 ]);
        // echo "1: lat " . $location[ "lat" ] . " long " . $location[ "lon" ] . "\n";
    }
    else
    {
        return null;
    }

    if ($latitude[ 2 ][ 0 ] && $latitude[ 2 ][ 0 ])
    {
        $location[ "lat" ] = floatval("" . $latitude[ 1 ][ 0 ] . $latitude[ 2 ][ 0 ]);
        $location[ "lon" ] = floatval("" . $longitude[ 1 ][ 0 ] . $longitude[ 2 ][ 0 ]) * -1;
        // echo "2: lat " . $location[ "lat" ] . " long " . $location[ "lon" ] . "\n";
    }

    return $location;
}

function getFiles($links)
{
    $files = array();

    foreach ($links as $key => $value)
    {
        preg_match_all("/(File:.*)/", $value, $match, PREG_PATTERN_ORDER);
        if ($match[ 1 ])
        {
            array_push($files, $match[ 1 ][ 0 ]);
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

    //
    //  https://en.wikipedia.org/w/api.php?action=query&titles=. $title . &prop=revisions&rvprop=content&format=json
    //  https://en.wikipedia.org/w/api.php?action=query&titles=London&prop=revisions&rvprop=content&format=json
    //

    $wiki = "https://en.wikipedia.org";

    $wikiJson = file_get_contents($wiki . "/w/api.php?action=query&titles=". $title . "&prop=revisions&rvprop=content&format=json");
    $wikiJson = json_decode($wikiJson, true);

    // $content = $wikiJson[ "query" ][ "pages" ][ "6097297" ][ "revisions" ][ 0 ][ "*" ];
    $content = $wikiJson[ "query" ][ "pages" ];

    if (count($content) == 0) return;

    foreach ($content as $key => $value)
    {
        $title = $value[ "title" ];
        $title = str_replace(" ", "_", $title);

        $resultJson= array();

        $resultJson[ "title" ] = $title;
        $resultJson[ "api"   ] = $wiki . "/w/api.php?action=query&titles=" . $title . "&prop=revisions&rvprop=content&format=json";
        $resultJson[ "wiki"  ] = $wiki . "/wiki/" . $title;
        $resultJson[ "key"   ] = $key;

        // echo "--> " . $title . "\n";

        $revisions = count($value[ "revisions" ]);

        if ($revisions > 1)
        {
            echo "revisions: $revisions\n";
            echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n";
            exit(-1);
        }

        $content = $value[ "revisions" ][ 0 ][ "*" ];
        $links   = getLinks($content);

        if (count($links) == 0) continue;

        $location = getLocation($content);

        if ($location)
        {
            echo "**> latitude:  " . $location[ "lat" ] . "\n";
            echo "**> longitude: " . $location[ "lon" ] . "\n";

            $resultJson[ "location" ] = $location;
        }

        $files = getFiles($links);
        $resultJson[ "files" ] = $files;

        $resultJson[ "linksCount" ] = count($links);
        $resultJson[ "links" ]      = $links;

        $destiantion = $title . ".json";
        $data = prettyJson($resultJson);

        writeFileDir("./Wiki/", $destiantion, $data);
        // writeFileDir("./Wiki-Source/", $destiantion, prettyJson($wikiJson));

        $server = "localhost";
        $index  = "wiki";
        $type   = "cloud";

        putData($data, $server, $index, $type);
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

    writeFile("nodes.json", prettyJson($result));

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

    writeFile("edges.json", prettyJson($result));
}

function stuff($name)
{
    getWikiJson($name);

    $links = getLinksRaw($name);

    foreach ($links as $key => $value)
    {
        getWikiJson($value);
    }
}


// stuff("New_York_City");
stuff("European_Union");
// stuff("Ebola_virus_disease");
// stuff("Battle_of_Long_Island");
// getWikiJson("Battle_of_Long_Island");
// stuff("London");
// getWikiJson("London");
// getWikiJson("New_York_City");
// curl -XPUT "http://localhost:9200/wiki?pretty" -d '{"mappings": { "cloud": { "properties" : {"location" : {"type" : "geo_point"}}}}}'
?>
