<?php

include("../../Lib.php");

header("Content-Type: text/plain");

$article = readJson("../Article/politics/2016/apr/24/barack-obama-post-brexit-trade-deal-with-uk-could-take-10-years.json");
// $article = readJson("../Article/us-news/2016/apr/24/barack-obama-such-power-such-humility.json");

$article[ "body" ] = deMoroniseHtmlForPage($article[ "body" ]);

echo prettyJson($article);

?>
