c:\programme\mplayer\ffmpeg.exe -y -i %1 -map 0:v -map 0:a -codec:v copy -codec:a copy -codec:s copy -f vob %1.vob
PAUSE