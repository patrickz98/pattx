<?php

exec("find Series-1/ -name '*.vob' -size +750000k |grep -E .vob > xxx.txt");
$i = 1;
$b = 1;
$zeilen = exec("cat xxx.txt |wc -l");

while($i < $zeilen)
{
	$txt = file('xxx.txt');
	//echo $txt[$i];

	//$done = fopen("done.txt", "w+")
	$done = file('done.txt');
	$donezeilen = exec("cat done.txt |wc -l");

	while($b > $donezeilen)
		if ($done[$b] == $txt[$i])
			{
			echo "+++++++++++++++++++++++++++++++++++";
			$i++;
			}
	echo $txt[$i];
	echo "ffmpeg\n";
	$i++;
}



?>
