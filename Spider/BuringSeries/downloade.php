<?php

include("../Lib.php");

//
// writeFileDir($dir, $destination, $content)
// https://bs.to/serie/Game-of-Thrones/6
//
//<a class="icon Vivo" title="Vivo" href="serie/Game-of-Thrones/6/1-Die-Rote-Frau/Vivo-1">Vivo</a>
//
// <a href="http://vivo.sx/4a4dd01678" target="_blank"><span class="icon link_go"></span> Link zum Originalvideo</a>
//

function downloade()
{
    echo " [Y/n] ";

    $handle = fopen("php://stdin", "r");
    $line = fgets($handle);

    if(trim($line) == "n")
    {
        return false;
    }
    else
    {
        return true;
    }
}

function options($serie, $season, $episodes)
{
    $data = "#!/bin/sh\n\n";

    $downloadeProxy = "sh downloade-proxy.sh";
    $seasonName = "$serie-$season";

    foreach ($episodes as $name => $url)
    {
        echo $name . ": " . $url;

        $downloade = downloade();

        if ($downloade)
        {
            $com  = $downloadeProxy . " \"$url\" " . "./$seasonName/$name";
            $data = $data . $com . "\n";
        }
    }

    $fileName = "./$seasonName.sh";
    echo "--> $fileName\n";

    $getSh = @fopen($fileName, "w");
    @fwrite($getSh, $data);
    @fclose($getSh);
}

function getName($episode)
{
    $dataArray = explode("/", $episode);
    return $dataArray[ count($dataArray) - 2 ];
}

function getSerie($serie, $season)
{
    echo "Collecting Informations ...\n";

    $bs = file_get_contents("https://bs.to/serie/$serie/$season");

    preg_match_all("/href=\"(.*?)\">Vivo<\/a>/", $bs, $result);

    $episodes = array();

    foreach ($result[ 1 ] as $key => $value)
    {
        $name = getName($value);
        $vivo = getVivo($value);

        $episodes[ $name ] = $vivo;
    }

    $dir = "./Series/";
    $destination = "$serie-$season.json";

    $content = prettyJson($episodes);

    writeFileDir($dir, $destination, $content);

    options($serie, $season, $episodes);
}

function getVivo($url)
{
    // $content = file_get_contents("https://bs.to/serie/Game-of-Thrones/6/1-Die-Rote-Frau/Vivo-1");
    $content = file_get_contents("https://bs.to/" . $url);

    preg_match_all("/<a href=\"(http:\/\/vivo.sx\/.*?)\"/", $content, $result);

    // print_r($result);

    return $result[ 1 ][ 0 ];
}

// https://bs.to/serie/Game-of-Thrones/6
// https://bs.to/serie/House-of-Cards-US/4
// Sherlock/3
// Homeland/5

getSerie("Game-of-Thrones",   "6");
getSerie("House-of-Cards-US", "4");
// getSerie("Sherlock",          "4");
getSerie("Homeland",          "5");

?>
