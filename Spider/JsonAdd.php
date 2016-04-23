<?php

class JsonAdd
{
    private $file     = null;
    private $jsonData = array();

    function __construct($file)
    {
        $this->file = $file;
        $content = @file_get_contents($file);

        if ($content != null)
        {
            $this->jsonData = json_decode($content, true);
        }
    }

    function isMember($obj)
    {
        if (in_array($obj, $this->jsonData))
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    function add($obj)
    {
        array_push($this->jsonData, $obj);
        sort($this->jsonData);
    }

    function close()
    {
        $myfile = @fopen($this->file, "w");
        @fwrite($myfile, prettyJson($this->jsonData));
        @fclose($myfile);
    }
}
?>
