<?php

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

        $links = getLinks($content = $value[ "revisions" ][ 0 ][ "*" ]);

        if (count($links) == 0) continue;

        $resultJson[ $title ][ "linksCount" ] = count($links);
        $resultJson[ $title ][ "links" ]      = $links;

        @mkdir($structure, 0777, true);

        $destiantion = $structure . str_replace("/", "_", $title);

        $myfile = @fopen($destiantion . ".json", "w");
        @fwrite($myfile, json_encode($resultJson[ $title ], JSON_PRETTY_PRINT));
        @fclose($myfile);
    }

    return $resultJson;
}

$tmp = getCoalitions("Linux");
$tmp = array_unique($tmp);
    // . "Barack_Obama|Harvard_Law_School|Angela_Merkel|"
    // . "Christian_Wulff|Hamburg|Chancellor_of_Germany|Helmut_Schmidt|"
    // . "Democratic_Party_(United_States)|White_House|Great_Recession");

// $file = fopen("./all.json", "w");
// fwrite($file, json_encode($tmp, JSON_PRETTY_PRINT));
// fclose($file);

foreach ($tmp as $key => $value)
{
    foreach ($value[ "links" ] as $link)
    {
        getCoalitions($link);
    }
}

?>
