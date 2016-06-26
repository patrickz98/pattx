<?php

include("../Lib.php");

function getSslPage($url)
{
    $header = array("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:45.0) Gecko/20100101 Firefox/45.0");

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
    curl_setopt($ch, CURLOPT_HEADER,         false);
    curl_setopt($ch, CURLOPT_USERAGENT,      'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13');
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_URL,            $url);
    curl_setopt($ch, CURLOPT_REFERER,        $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);

    curl_setopt($ch, CURLOPT_AUTOREFERER,    TRUE);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);


    $result = curl_exec($ch);

    curl_close($ch);

    return $result;
}

function replaceLinks($content)
{
    preg_match_all("/<a href=\"(.*?)\".*?>(.*?)<\/a>/", $content, $links);

    $content = preg_replace("/(<.*?>)/", "", $content);
    return $content;
}

function getHeadline($content)
{
    preg_match_all("/<h1.*?id=\"headline\".*?>(.*?)<\/h1>/", $content, $headline);
    return $headline[ 1 ][ 0 ];
}

function getContent($content)
{
    preg_match_all("/<p class=\"story-body-text story-content\".*?>(.*?)<\/p>/", $content, $result);
    // print_r($result[ 1 ]);
    $result = $result[ 1 ];

    $article = "";

    foreach ($result as $key => $value)
    {
        $article = $article . deMoroniseHtml($value) + "\n\n";
    }
    return $article;
}

function getMeta($content, $name, $array = false)
{
    // preg_match_all("/<meta name=\"" . $name . "\" content=\"(.*?)\"/", $content, $result);
    // preg_match_all("/<meta name=\"(.*?)\" content=\"(.*?)\"/", $content, $result);
    preg_match_all("/<meta name=\"" . $name . "\" content=\"(.*?)\"/", $content, $result);
    // preg_match_all("/(<meta.*>)/", $content, $result);

    // print_r($result);
    if ($array)
    {
        return $result[ 1 ];
    }
    else
    {
        return $result[ 1 ][ 0 ];
    }
}

function getMetaSplite($content, $name)
{
    $data = getMeta($content, $name);
    $data = explode(",", $data);

    return $data;
}

function main($url)
{
    // $url = "http://www.nytimes.com/2016/04/17/opinion/sunday/why-americans-cant-vote.html";
    // $url = "donald-trump-foreign-policy-speech.html";
    // $content = file_get_contents($url);
    $content = getSslPage($url);

    $fileName = $url;
    $fileName = str_replace("http://www.",  "",  $fileName);
    $fileName = str_replace("/",  "_",  $fileName);
    writeFile($fileName . ".html", $content);

    $json = array();
    $json[ "headline" ] = getHeadline($content);
    $json[ "Content"  ] = getContent($content);

    $json[ "sourceApp"     ] = getMeta($content, "sourceApp");
    $json[ "hdl"           ] = getMeta($content, "hdl");
    $json[ "col"           ] = getMeta($content, "col");
    $json[ "pdate"         ] = getMeta($content, "pdate");
    $json[ "utime"         ] = getMeta($content, "utime");
    $json[ "ptime"         ] = getMeta($content, "ptime");
    $json[ "DISPLAYDATE"   ] = getMeta($content, "DISPLAYDATE");

    $json[ "dat"           ] = getMeta($content, "dat");
    $json[ "lp"            ] = getMeta($content, "lp");
    $json[ "cre"           ] = getMeta($content, "cre");
    $json[ "author"        ] = getMeta($content, "author");
    $json[ "tone"          ] = getMeta($content, "tone");

    $json[ "byl"           ] = getMeta($content, "byl");
    $json[ "PT"            ] = getMeta($content, "PT");
    $json[ "CG"            ] = getMeta($content, "CG");
    $json[ "SCG"           ] = getMeta($content, "SCG");
    $json[ "PST"           ] = getMeta($content, "PST");
    $json[ "tom"           ] = getMeta($content, "tom");
    $json[ "edt"           ] = getMeta($content, "tom");

    $json[ "geo"           ] = getMeta($content, "geo");
    $json[ "des"           ] = getMeta($content, "des", true);

    $json[ "keywords"      ] = getMetaSplite($content, "keywords");
    $json[ "news_keywords" ] = getMetaSplite($content, "news_keywords");

    $fileName = $fileName . ".json";

    echo "$fileName\n";
    // writeFile("test.json", prettyJson($json));
    writeFile($fileName, prettyJson($json));

    // $date = DateTime::createFromFormat("Ymd", "20160416");
    // echo $date->format('Y-m-d') . "\n";
    // $json[ "date"     ] = getContent($content);
}

// main("http://www.nytimes.com/2016/04/28/us/politics/donald-trump-foreign-policy-speech.html");
// main("http://www.nytimes.com/2016/04/17/opinion/sunday/why-americans-cant-vote.html");
main("http://www.nytimes.com/2016/04/28/us/politics/ted-cruz-carly-fiorina.html");


?>
