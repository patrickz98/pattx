<?php

// include("../Lib.php");

function getSslPage($url)
{
    $header = array("X-Secret: ef1829653048e7db10ebb30f82a48607b7242ae1af9b7acacd7c1997e8933a81");

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_HEADER,         false);
    curl_setopt($ch, CURLOPT_HTTPHEADER,     $header);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_URL,            $url);
    curl_setopt($ch, CURLOPT_REFERER,        $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);

    $result = curl_exec($ch);

    curl_close($ch);

    return $result;
}

function getPronunciation($fileName, $id, $pron)
{
    $url = "http://sounds.pons.com/audio_tts/$pron/$id";
    $dir = "./Audio/";

    $file = "$id-$pron.mp3";

    writeFileDir($dir, $file, getSslPage($url));

    return $dir . $file;
}

function ponsJson($word, $audio = ture)
{
    if (is_numeric($word)) return;

    // $url = "https://api.pons.com/v1/dictionary?q=" . $title . "&l=deen&in=&lf=en";
    // $url = "https://api.pons.com/v1/dictionary?q=" . $title . "&l=deen&in=de&lf=en";
    $url = "https://api.pons.com/v1/dictionary?q=" . urlencode($word) . "&l=deen";

    $result = getSslPage($url);

    if ($result == null)
    {
        // echo "{ \"Error\": \"$word\"}";
        return;
    }

    $urlJson = json_decode($result, true);

    if ($urlJson == null)
    {
        // echo "++> json Error: $word\n";
        return;
    }

    $CombinedJson = array();
    $CombinedJson[ $word ] = array();

    foreach ($urlJson as $key => $trans)
    {
        foreach ($trans[ "hits" ] as $key2 => $value)
        {

            if (! array_key_exists("roms", $value)) continue;

            foreach ($value[ "roms" ] as $key3 => $rom)
            {
                $headword = $rom[ "headword" ];
                $headword = str_replace("\\u00b7", "", $headword);
                $headword = str_replace("\\u02c8", "", $headword);
                $headword = str_replace("·",       "", $headword);
                $headword = str_replace("ˈ",       "", $headword);

                $transJson = array();
                $transJson[ $headword ] = array();
                $transJson[ $headword ][ "wordclass"   ] = $rom[ "wordclass" ];
                $transJson[ $headword ][ "translation" ] = array();

                if (count($rom[ "arabs" ]) == 0) continue;

                foreach ($rom[ "arabs" ] as $key4 => $arab)
                {
                    if (count($arab[ "translations" ]) == 0) continue;

                    foreach ($arab[ "translations" ] as $key5 => $translation)
                    {
                        $trans = array();

                        $id     = $translation[ "id"     ];
                        $source = $translation[ "source" ];
                        $target = $translation[ "target" ];

                        $trans[ "id"     ] = $id;
                        $trans[ "source" ] = deMoroniseHtml($source);
                        $trans[ "target" ] = deMoroniseHtml($target);

                        if ($trans[ "source" ] == "" && $trans[ "target" ] == "")
                        {
                            continue;
                        }

                        if ($audio)
                        {
                            $trans[ "audio"  ] = array();
                            array_push($trans[ "audio" ], getPronunciation(null, $id, "en_gb"));
                            array_push($trans[ "audio" ], getPronunciation(null, $id, "en_us"));
                            array_push($trans[ "audio" ], getPronunciation(null, $id, "de"));
                        }

                        array_push($transJson[ $headword ][ "translation" ], $trans);
                    }
                }

                array_push($CombinedJson[ $word ], $transJson);
            }
        }
    }

    // $data = json_encode($urlJson, JSON_PRETTY_PRINT);
    // $file = $word . ".ori.json";
    // writeFileDir("./Translation/", $file, $data);

    return $CombinedJson;
}

function dic($id)
{
    $endpoint = "https://api.pons.com/v1/dictionaries?language=";
    $result   = getSslPage($endpoint . $id);
    $result   = niceJson($result);

    writeFileDir("./Dics/", $id . ".json", $result);
}

function getDics()
{
    dic("de");
    dic("el");
    dic("en");
    dic("es");
    dic("fr");
    dic("it");
    dic("pt");
    dic("ru");
    dic("sl");
    dic("tr");
    dic("zh");
}

// getDics();

// ponsJson($argv[ 1 ]);
// ponsJson("House");

?>
