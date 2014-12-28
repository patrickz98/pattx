<!DOCTYPE html>
<html>
    <head>
    	<link type='text/css' rel='stylesheet' href='style.css'/>
	<title>Coin Flips</title>
	</head>
	<body>
	<?php

	$headCount = rand(50, 160);

	echo "<h1>" . "Points" . "</h1>";

	while ($headCount != 1)
	{
	        $rand = rand(25, 160);
	        $rand2 = $rand / 2;
	        $opt = "height: {$rand}px;
	                width: {$rand}px;
	                border-radius: {$rand2}px;
	                background-color: gray;
	                text-align: center;
	                font-weight: bold;
	                font-family: sans-serif;
	                color: white;
	                margin: 10px;
	                display: inline-block;
	                line-height: 50px;
	                font-size: 20px;";

		$headCount--;
		echo "<div style=\"$opt\">" . $headCount  . "</div>\n";
	}
	?>
    </body>
</html>
