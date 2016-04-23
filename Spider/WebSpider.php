<?php

include("./Lib.php");
// include("./JsonAdd.php");

function openUrl($url)
{
    echo "--> $url\n";

    $content = @file_get_contents($url);

    // preg_match_all("/\"(http:\/\/.*?)\"/", $content, $find, PREG_PATTERN_ORDER);
    // print_r($find);
    // return;


    if ($content == null) return;

    // (\.html|\.php|\.htm|\.htn)
    preg_match_all("/\"(http:\/\/.*?)\"/", $content, $find, PREG_PATTERN_ORDER);

    // print_r($find[ 0 ]);

    foreach ($find[ 1 ] as $key => $value)
    {
        $add = addJson("./Links.json", $value);

        if ($add)
        {
            echo "--> $value\n";
        }
    }
}

$links = readJson("./Links.json");

foreach ($links as $key => $value)
{
    openUrl($value);
}

// openUrl("http://www.spiegel.de/");
// openUrl("https://www.google.de/?gfe_rd=cr&ei=omQWV7T8HcGF8Qe3nIKgDA#q=Patrick+Zierahn");
// openUrl("http://www.nytimes.com/");
// openUrl("http://www.theguardian.com/international");
// openUrl("http://www.latimes.com");

?>
