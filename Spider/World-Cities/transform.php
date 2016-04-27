<?php

include("../Spider/Lib.php");
include("../Spider/Elastic.php");

//
// https://github.com/playthecall/playthecall/raw/master/db/resources/worldcitiespop.txt.gz
// worldcitiespop.txt
// Country,City,AccentCity,Region,Population,Latitude,Longitude
//

$globalTmp = readJson("Countrys.json");
$global = array();

foreach ($globalTmp as $key => $value)
{
    $nameAlpha = strtolower($value[ "alpha-2" ]);

    $global[ $nameAlpha ] = array();
    $global[ $nameAlpha ][ "country"    ] = $value[ "name" ];
    $global[ $nameAlpha ][ "alpha-2"    ] = $value[ "alpha-2" ];
    $global[ $nameAlpha ][ "alpha-3"    ] = $value[ "alpha-3" ];
    $global[ $nameAlpha ][ "region"     ] = $value[ "region" ];
    $global[ $nameAlpha ][ "sub-region" ] = $value[ "sub-region" ];
}

$file = new SplFileObject("worldcitiespop.txt");
$inx = 0;

while (! $file->eof())
{
    $data = $file->fgets();
    $dateArray = explode(",", $data);

    // print_r($dateArray);

    $alpha2     = utf8_encode($dateArray[ 0 ]);
	$Country    = $global[ $alpha2 ][ "country" ];

    $City       = utf8_encode($dateArray[ 1 ]);
    $AccentCity = utf8_encode($dateArray[ 2 ]);
    $Region     = utf8_encode($dateArray[ 3 ]);
    $Population = floatval(   $dateArray[ 4 ]);
    $Latitude   = floatval(   $dateArray[ 5 ]);
    $Longitude  = floatval(   $dateArray[ 6 ]);

	if ($Population == 0)
	{
		$Population = null;
	}

	if ($Region == "")
	{
		$Region = null;
	}

	$json = array();
	$json[ "Country"    ] = $Country;
	$json[ "alpha-2"    ] = $alpha2;
	$json[ "region"     ] = $global[ $alpha2 ][ "region" ];
    $json[ "City"       ] = $City;
    $json[ "AccentCity" ] = $AccentCity;
    $json[ "Region"     ] = $Region;
    $json[ "Population" ] = $Population;
    $json[ "location"   ] = array();
    $json[ "location"   ][ "lat" ] = $Latitude;
    $json[ "location"   ][ "lon" ] = $Longitude;

    if ($Region != null)
	{
    	$dir = "./map/" . $alpha2 . "/" . $Region . "/";
	}
	else
	{
	    $dir = "./map/" . $alpha2 . "/";
	}

    $fileName = $AccentCity . ".json";

    $json = prettyJson($json);
    // writeFileDir($dir, $fileName, $json);

    $server = "localhost";
    $index  = "map";
    $type   = "testing";

    putData($json, $server, $index, $type);

    $inx++;
    printf("%s %-6f%%\r", $alpha2, ($inx / 3173958) * 100);
}

echo "\nDone...\n";

?>
