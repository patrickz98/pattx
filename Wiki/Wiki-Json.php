<?php

function getJson($title)
{
    $wiki = "https://en.wikipedia.org";

    $wikiJson = file_get_contents($wiki . "/w/api.php?action=query&titles=". $title . "&prop=revisions&rvprop=content&format=json");
    $wikiJson = json_decode($wikiJson, true);
    $wikiJson = json_encode($wikiJson, JSON_PRETTY_PRINT);


    $myfile = @fopen($title . ".json", "w");
    @fwrite($myfile, $wikiJson);
    @fclose($myfile);
}

getJson($argv[ 1 ]);
?>
