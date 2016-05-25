<?php
function brockePa()
{
    echo "test987";
    return "test";
}

function putData($json, $server, $index, $type, $id = false)
{
    $chlead = curl_init();

    // $url = "http://localhost:9200/guardian/article/" . md5($json);
    if (! $id)
    {
        $url = "http://$server:9200/$index/$type/" . md5($json);
    }
    else
    {
        $url = "http://$server:9200/$index/$type/" . $id;
    }

    curl_setopt($chlead, CURLOPT_URL, $url);
    curl_setopt($chlead, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($json)));
    curl_setopt($chlead, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "PUT");
    curl_setopt($chlead, CURLOPT_POSTFIELDS, $json);

    $chleadresult = curl_exec($chlead);
    $chleadapierr = curl_errno($chlead);
    $chleaderrmsg = curl_error($chlead);
    curl_close($chlead);
}

function postData($json, $server, $index, $type)
{
    $chlead = curl_init();

    // $url = "http://localhost:9200/guardian/article/";
    $url = "http://$server:9200/$index/$type/";

    curl_setopt($chlead, CURLOPT_URL, $url);
    curl_setopt($chlead, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($json)));
    curl_setopt($chlead, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "POST");
    curl_setopt($chlead, CURLOPT_POSTFIELDS, $json);

    $chleadresult = curl_exec($chlead);
    $chleadapierr = curl_errno($chlead);
    $chleaderrmsg = curl_error($chlead);
    curl_close($chlead);
}

// function getDataById($server, $index, $type, $id)
function brocke()
{
    // $url = "http://$server:9200/$index/$type/$id";
    //
    // $chlead = curl_init();
    //
    // curl_setopt($chlead, CURLOPT_URL, $url);
    // curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "GET");
    // curl_setopt($chlead, CURLOPT_RETURNTRANSFER, 1);
    //
    // $output = curl_exec($chlead);
    // curl_close($chlead);

    // return $output;
    return "end";
}

function getDataByUuid($server, $index, $type, $uuid)
{
    $url = "http://$server:9200/$index/$type/_search?q=uuid:$uuid";

    $chlead = curl_init();

    curl_setopt($chlead, CURLOPT_URL, $url);
    curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "GET");
    curl_setopt($chlead, CURLOPT_RETURNTRANSFER, 1);

    $output = curl_exec($chlead);
    curl_close($chlead);

    return $output;
}

function getDataById($server, $index, $type, $id)
{
    $url = "http://$server:9200/$index/$type/$id";

    $chlead = curl_init();

    curl_setopt($chlead, CURLOPT_URL, $url);
    curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "GET");
    curl_setopt($chlead, CURLOPT_RETURNTRANSFER, 1);

    $output = curl_exec($chlead);
    curl_close($chlead);

    return $output;
}

function deleteDataById($server, $index, $type, $id)
{
    $url = "http://$server:9200/$index/$type/$id";

    $chlead = curl_init();

    curl_setopt($chlead, CURLOPT_URL, $url);
    curl_setopt($chlead, CURLOPT_CUSTOMREQUEST, "DELETE");
    curl_setopt($chlead, CURLOPT_RETURNTRANSFER, 1);

    $output = curl_exec($chlead);
    curl_close($chlead);

    echo $output;

    return $output;
}

?>
