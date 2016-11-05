#!/bin/bash

HM=$(date +"%H_%M")
echo $HM
stream=$(curl -s http://cdn08.vtomske.ru/hls/stream6.m3u8|grep stream|head -n 1)
echo $stream
curl -s http://cdn08.vtomske.ru/hls/$stream > temp.ts
ffmpeg -loglevel panic -i "temp.ts" -filter:v "crop=28:16:1099:491" "temp_cropped.mp4"
ffmpeg -loglevel panic -i "temp_cropped.mp4" -vf fps=1 "$1/$HM-%d.png"
rm temp.ts temp_cropped.mp4

