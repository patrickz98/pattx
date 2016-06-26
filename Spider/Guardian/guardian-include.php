<?php

function getLinks($content)
{
    preg_match_all("/<a href=\"x-gu:\/\/list\/(.*?)\"/", $content, $resultList);
    preg_match_all("/<a href=\"x-gu:\/\/item\/mobile-apps\.guardianapis\.com\/items\/(.*?)\"/", $content, $resultItems);

    if (count($resultList[ 1 ]) > 0)
    {
        $testClass = new JsonAdd("./Headlines-list.json");

        foreach ($resultList[ 1 ] as $key => $value)
        {
            $find = "http://" . $value;

            if (! $testClass->isMember($find))
            {
                echo "--> New Headline: $find\n";
                $testClass->add($find);
            }
        }

        $testClass->close();
    }

    // print_r($resultItems[ 1 ]);

    // if (count($resultItems[ 1 ]) > 0)
    // {
    //     foreach ($resultItems[ 1 ] as $key => $value)
    //     {
    //         echo "++> $value\n";
    //         // getArticle($value);
    //     }
    // }
}

function collectWords($body)
{
    $testClass = new JsonAdd("./Word-list.json");

    $result = deMoroniseHtml($body);
    $result = deMoroniseBody($result);

    $result = explode(" ", $result);
    $result = array_unique($result);

    foreach ($result as $key => $value)
    {
        if (preg_match("/.*[0-9]|[0-9].*/", $value))
        {
            continue;
        }

        if (preg_match("/&.*?;/", $value))
        {
            continue;
        }

        if (preg_match("/^[A-Z].*?[A-Z].*?$/", $value))
        {
            continue;
        }

        if ((strlen($value) > 3) && (! $testClass->isMember($value)))
        {
            $testClass->add($value);
        }
    }

    $testClass->close();
}

function getArticle($title, $dir = "./Article/")
{
    $url = "http://mobile-apps.guardianapis.com/items/" . $title;

    $dataJson = @file_get_contents($url);

    if ($dataJson == null)
    {
        echo "++> 404 $url\n";
        return;
    }

    $dataJson = json_decode($dataJson, true);

    $structure = explode("/", $title);

    $fileName = $structure[ count($structure) - 1 ];
    $fileName = $fileName . ".json";

    $dataJson[ "file" ] = $dir . $fileName;
    $dataJson[ "category" ] = $structure[ 0 ];

    $writeJson = prettyJson($dataJson);
    writeFileDir($dir, $fileName, $writeJson);

    $server = "localhost";
    $index  = "guardian";
    $type   = "article";

    putData($writeJson, $server, $index, $type);

    addJson("./Article-list.json", $url);

    if (! array_key_exists("body", $dataJson)) return;

    $body = $dataJson[ "body" ];
    getLinks($body);
    // collectWords($body);
}

function cards($url)
{
    echo "--> $url\n";
    $contentArray = @file_get_contents($url);

    if ($contentArray == null)
    {
        echo "++> 404 $url\n";
        return;
    }

    $contentArray = json_decode($contentArray, true);

    $fileName = str_replace("http://", "", $url);
    $fileName = str_replace("/", "_", $fileName);
    $fileName = $fileName . ".json";

    writeFileDir("./Headlines/", $fileName, prettyJson($contentArray));

    if (addJson("./Headlines-list.json", $url))
    {
        echo "--> New Headline: $url\n";
    }

    if (! array_key_exists("cards", $contentArray)) return;

    $cards = $contentArray[ "cards" ];

    if (count($cards) == 0) return;

    $article = array();

    foreach ($cards as $key => $card)
    {
        $id = $card[ "item"  ][ "id" ];
        // $dirPath = explode("/", $id);
        //
        // // remove /.*?.html
        // unset($dirPath[ count($dirPath) - 1 ]);

        $dir = "./Article/" . removeHtmlSuffix($id) . "/";

        getArticle($id, $dir);

        array_push($article, $id);
    }

    return $article;
}

function getHeadlines($url, $recusive = false)
{
    $urlJson  = file_get_contents($url);
    $JsonData = json_decode($urlJson, true);
    $urlJson  = niceJson($urlJson);

    // "pagination": {
    //     "currentPage": 1,
    //     "totalPages": 18,
    // }

    $fileName = str_replace("http://", "", $url);
    $fileName = str_replace("/", "_", $fileName);
    $fileName = $fileName . ".json";

    writeFileDir("./Headlines/", $fileName, $urlJson);

    if ($recusive && $JsonData[ "pagination" ][ "totalPages" ])
    {
        for ($inx = 0; $inx < $JsonData[ "pagination" ][ "totalPages" ]; $inx++)
        {
            getHeadlines($url . "?page=" . ($inx + 1), false);
        }
    }

    getSubContent($url);
}

function home()
{
    $urlJson  = file_get_contents("http://mobile-apps.guardianapis.com/uk/fronts/home");
    $JsonData = json_decode($urlJson, true);

    if (! array_key_exists("layout", $JsonData))
    {
        echo "++> No layout.\n";
    }

    $entry = $JsonData[ "layout" ];

    if (count($entry) == 0) return;

    $cards = array();

    foreach ($entry as $key => $card)
    {
        $id = $card[ "id" ];

        cards("http://mobile-apps.guardianapis.com/$id");
    }
}

?>
