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

        if ($id == $level)
        {
            $level += $split;
            $main  += 1;

            $newArray[ $main ] = array();
        }
    }

    return $newArray;
}

function getLocation($content)
{
    // |Latitude = 40\u00b0\u200a30\u2032 N to 45\u00b0\u200a1\u2032 N\n|Longitude = 71\u00b0\u200a51\u2032 W to 79\u00b0\u200a46\u2032 W\n|
    // preg_match_all("/\|Latitude = (.*?)\|Longitude = (.*?)\|/", $content, $match, PREG_PATTERN_ORDER);

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

function getCoalitions($title)
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

        $files = getFiles($links);
        $resultJson[ $title ][ "files" ] = $files;

        $resultJson[ $title ][ "linksCount" ] = count($links);
        $resultJson[ $title ][ "links" ]      = $links;

        @mkdir($structure, 0777, true);

        $destiantion = $structure . str_replace("/", "_", $title);
        $myfile = @fopen($destiantion . ".json", "w");
        @fwrite($myfile, json_encode($resultJson[ $title ], JSON_PRETTY_PRINT));
        @fclose($myfile);

        @mkdir("./TXT/", 0777, true);

        $destiantion = "./TXT/" . str_replace("/", "_", $title);
        $myfile = @fopen($destiantion . ".txt", "w");
        @fwrite($myfile, $content);
        @fclose($myfile);
    }

    return $resultJson;
}

$startTime = time();

$count = 0;
$tmp = getCoalitions("New_York");
// $tmp = getCoalitions("New_York|United_States|Nobel_Peace_Prize|Hillary_Clinton|GDP|"
//     . "John_Kerry|Republican_Party_(United_States)|Bill_Clinton|United_States_Congress|"
//     . "Barack_Obama|Harvard_Law_School|Angela_Merkel|"
//     . "Christian_Wulff|Hamburg|Chancellor_of_Germany|Helmut_Schmidt|"
//     . "Democratic_Party_(United_States)|White_House|Great_Recession");

foreach ($tmp as $key => $value)
{
    $links = $value[ "links" ];
    $links = splitArray($links, 50);

    foreach ($links as $index => $link)
    {
        $link = join('|', $link);
        getCoalitions($link);
    }

    if (count($value[ "links" ]) == 0) continue;
    $count += count($value[ "links" ]) + 1;
}

echo "count: $count\n";
echo "time: " . (time() - $startTime) . "\n";

?>
