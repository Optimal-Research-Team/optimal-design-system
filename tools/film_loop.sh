#!/bin/zsh
# film_loop.sh in.mp4 out.mp4 [crossfade seconds, default 1.5]
# Makes a brand film loop without a seam: the last X seconds are crossfaded into the first X,
# so the final frame is the opening frame. 1280x720, H.264, no audio, faststart, about 0.6 MB
# for an 8 s source. Needs ffmpeg and ffprobe.
IN=$1; OUT=$2; X=${3:-1.5}
L=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$IN")
OFF=$(python3 -c "print(round($L-$X-$X,3))")
ffmpeg -v error -y -i "$IN" -filter_complex "[0:v]split[a][b];[a]trim=start=$X,setpts=PTS-STARTPTS[m];[b]trim=0:$X,setpts=PTS-STARTPTS[h];[m][h]xfade=transition=fade:duration=$X:offset=$OFF,scale=1280:-2,format=yuv420p[v]" \
  -map "[v]" -an -c:v libx264 -preset slow -crf 23 -profile:v high -movflags +faststart -r 24 "$OUT"
