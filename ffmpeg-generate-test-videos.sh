#!/bin/bash

## This script generates h.264 video files that contain HD Bars and Tone using FFmpeg and overlays the frame count and timecode data
## Global variables are included at the top of the script for quick customization

video_duration="10" #duration here is in seconds
font_size="50"
font_family_path="/Library/Fonts/Arial.ttf"
frame_rate_array=("23.976" "24" "25" "29.97_NDF" "29.97_DF" "30" "50" "59.94_NDF" "59.94_DF" "60")

format_frame_rate () {

    frame_rate_ffmpeg=${1//_*} # remove '_NDF' or '_DF' from frame_rate string for proper formatting in ffmpeg
    frame_rate_filename=${1//.} # remove '.' from frame rate to avoid issues with filenames
    
    #formatting filename to be a bit cleaner
    if [[ $1 == *"NDF" ]]; then
        frame_rate_filename=${frame_rate_filename//_NDF/_fps_NDF}
    elif [[ $1 == *"DF" ]]; then
        frame_rate_filename=${frame_rate_filename//_DF/_fps_DF}
    fi
}

filter_timecode () {
    # determine proper timecode format based on 'NDF' or 'DF' present in frame_rate string
    if [[ $1 == *"NDF" ]]; then
        start_timecode="00:00:00;00"
    else
        start_timecode="00:00:00:00"
    fi
}

format_timecode_for_drawtext () {
    # format timecode for ffmpeg filter, ex: '00:00:00:00' becomes '00\:00\:00\:00'
    escaped_timecode=${1//:/\\:} # escape ':' with '\:'
    escaped_timecode=${escaped_timecode//;/\\;} # escape possible ';' with '\;'
}  

for frame_rate in ${frame_rate_array[@]}; do

    format_frame_rate $frame_rate
    filter_timecode $start_timecode
    format_timecode_for_drawtext $start_timecode
    
    ffmpeg -f lavfi -i smptehdbars=duration=$video_duration:size=1280x720:rate=$frame_rate_ffmpeg \
    -f lavfi -i sine=frequency=1000:sample_rate=48000:duration=$video_duration \
    -vf "[in]drawtext=fontfile=$font_family_path:fontsize=$font_size:text='Frame\: %{frame_num}':start_number=0: \
    x=(w-tw)/2:y=h-(2*lh):fontcolor=white:box=1:boxcolor=black:boxborderw=4, \
    drawtext=fontfile=$font_family_path:fontsize=$font_size:'timecode=$escaped_timecode':rate=$frame_rate_ffmpeg: \
    x=(w-tw)/2:y=h-(2*lh)-$font_size:fontcolor=white:box=1:boxcolor=black:boxborderw=4[out]" \
    -c:v libx264 -pix_fmt yuv420p -preset ultrafast -crf 22 -c:a aac \
    -timecode $start_timecode "${frame_rate_filename}_sample_video".mp4

done
