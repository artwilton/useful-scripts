"""
This script uses the subprocess module to run custom ffmpeg commands from a python script which is
useful when you need to run complex commands and want something more flexible than a shell script

A tip for making this script more useful would be to add more variables for things like the output
codecs for video and audio, preset speed, crf rate, output resolution, etc. and then building a prompt
to grab user input, passing the result to those variables
"""

import subprocess

## replace this with path for your ffmpeg binary if you're not using homebrew on MacOS
ffmpeg = "/usr/local/bin/ffmpeg"
input_file = "/path/to/input/file"
output_file = "path/to/desired/output/output_file.ext"

## ffmpeg commands to use, commands should each be a string entered in a list, example command:
## [ffmpeg, "-i", input_file, "-c:v", "libx264", "-preset", "fast", "-crf", "22", "-s", "1280x720", "-c:a", "aac", "-b:a", "196k", "-ar", "44100", "-pix_fmt", "yuv420p", output_file]
commands_list = []

def runFFmpeg(commands):
    if subprocess.run(commands).returncode == 0:
        print ("FFmpeg Script Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script")

runFFmpeg(commands_list)