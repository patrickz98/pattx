<?php

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

?>
