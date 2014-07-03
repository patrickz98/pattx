c:\programme\mplayer\ffmpeg.exe -y -i %1 -map 0:0 -map 0:1 -map 0:2 -map 0:3 -map 0:4 -map 0:5 -codec:v copy -codec:a copy -codec:s copy -f vob %1.vob
IF NOT ERRORLEVEL 0 EXIT /b 1
PAUSE