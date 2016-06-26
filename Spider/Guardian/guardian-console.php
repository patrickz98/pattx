<?php

include("../Lib.php");
include("../JsonAdd.php");
include("../Pons/pons-include.php");
include("../Elastic.php");

include("./guardian-include.php");

function headlineCards()
{
    $list = readJson("Headlines-list.json");

    foreach ($list as $key => $headline)
    {
        cards($headline);
    }
}

// home();
headlineCards();
// home();
// getHeadlines("http://mobile-apps.guardianapis.com/uk/groups/collections/uk-alpha/news/regular-stories");
// getHeadlines("http://mobile-apps.guardianapis.com/lists/tag/us-news/donaldtrump", true);


// getJson("http://mobile-apps.guardianapis.com/uk/groups/collections/uk-alpha/news/regular-stories");
// getArticle("world/video/2016/feb/26/former-mexican-president-vicente-fox-trump-we-wont-pay-for-the-wall-video");

?>
