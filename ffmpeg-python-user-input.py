import subprocess

## defualts
ffmpeg = "/usr/local/bin/ffmpeg"
input_file = ""
output_file = "~/Desktop"
video_codec = "libx264"
audio_codec = "aac"
audio_bitrate = "196k"
sample_rate = "44100"
encoding_speed = "fast"
crf_factor = "22"

commands_list = []

## ffmpeg commands to use, commands should each be a string entered in a list, example command:
## [ffmpeg, "-i", input_file, "-c:v", "libx264", "-preset", "fast", "-crf", "22", "-s", "1280x720", "-c:a", "aac", "-b:a", "196k", "-ar", "44100", "-pix_fmt", "yuv420p", output_file]

def runFFmpeg(commands):
    if subprocess.run(commands).returncode == 0:
        print ("FFmpeg Script Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script")

runFFmpeg(commands_list)