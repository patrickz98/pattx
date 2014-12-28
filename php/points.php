<!DOCTYPE html>
<html>
    <head>
    	<link type='text/css' rel='stylesheet' href='style.css'/>
	<title>Points</title>
	</head>
	<body>
	<?php

	$opt = "height: 50px;
		width: 50px;
		border-radius: 25px;
		background-color: gray;
		text-align: center;
		font-weight: bold;
		font-family: sans-serif;
		color: white;
		margin: 10px;
		display: inline-block;
		line-height: 50px;
		font-size: 20px;";

	$headCount = rand(50, 160);

	echo "<h1>" . "Points" . "</h1>";

	while ($headCount != 1)
	{
		$headCount--;
		echo "<div class=\"coin\">" . $headCount  . "</div>";
	}
	?>
    </body>
</html>
