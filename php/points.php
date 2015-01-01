<!DOCTYPE html>
<html>
    <head>
		<title>Points</title>
<!-- 
		 <meta http-equiv="refresh" content="2"> 
 -->
	</head>
	<body>
	<?php

	echo "<h1>" . "Points" . "</h1>\n";

	for($headCount = 0; $headCount < 25; $headCount++)
	{
			$color = array("gray", "gray", "yellow", "red", "navy", "lawngreen", "gold");
			$color_use = $color[rand(0, count($color))];

	        $rand = rand(25, 160);
	        $rand2 = $rand / 2;

	        $opt = "height: {$rand}px;
	                width: {$rand}px;
	                border-radius: {$rand2}px;
	                background-color: {$color_use};
	                text-align: center;
	                font-weight: bold;
	                font-family: sans-serif;
	                color: {$color_use};
	                margin: 10px;
	                display: inline-block;
	                line-height: 50px;
	                font-size: 20px;";

		echo "\t\t<div style=\"$opt\"></div>\n";
	}
	?>
    </body>
</html>
