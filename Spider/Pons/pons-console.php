<?php
include("../Lib.php");
include("./pons-include.php");

function getJsonWords()
{
    $list = readJson("./Word-list.json");

    foreach ($list as $key => $word)
    {
        $trans = ponsJson($word, false);
        $trans = prettyJson($trans);

        if ($trans == "null") continue;

        echo "./Translations/$word.json\n";
        writeFileDir("./Translations/", "$word.json", $trans);
    }
}

// http://sounds.pons.com/audio_tts/de/Tdeen273190
// http://sounds.pons.com/audio_tts/de/Tdeen29917260


// http://sounds.pons.com/audio_tts/es_mx/Tdees3821156
// http://sounds.pons.com/audio_tts/es_es/Tdees3821156
// getJsonWords();

$trans = ponsJson($argv[ 1 ], false);
$trans = prettyJson($trans);

echo "$trans\n";

// writeFileDir("./Translations/", "groß.json", ponsJson("groß"));
?>
