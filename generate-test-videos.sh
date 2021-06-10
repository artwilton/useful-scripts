#!/bin/bash

video_duration="60"
font_size="72"
font_family_path="/Library/Fonts/Arial.ttf"
frame_rate_array=("23.976" "24" "25" "29.97_NDF" "29.97_DF" "30" "50" "59.94_NDF" "59.94_DF" "60")

for frame_rate in ${frame_rate_array[@]}; do
    
    if [[ "$frame_rate" == *"NDF" ]]; then
        start_timecode="00:00:00;00"
    else
        start_timecode="00:00:00:00"
    fi

    # removes the '.' and '_NDF' or '_DF' from frame_rate string for proper formatting in ffmpeg
    frame_rate_name=${frame_rate//.}
    frame_rate=$(sed 's/_.*//' <<< $frame_rate)

    ffmpeg -t $video_duration -f lavfi -i smptebars=duration=10:size=1280x720:rate=$frame_rate \
    -vf "drawtext=fontfile=$font_family_path:text='Frame\: %{frame_num}':start_number=0:x=(w-tw)/2:y=h-(2*lh):fontcolor=white:fontsize=$font_size" \
    -c:v libx264 -timecode $start_timecode -pix_fmt yuv420p "${frame_rate_name}_fps_sample_video".mp4
done