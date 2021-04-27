## This script uses the subprocess module to run custom ffmpeg commands from a python script
## useful when you need to run complex commands and want something more flexible than a shell script

import subprocess

## replace this with path for your ffmpeg binary if you're not using homebrew on MacOS
ffmpeg = "/usr/local/bin/ffmpeg"

## ffmpeg commands to use, commands should each be a string entered in a list, example command:
## [ffmpeg, "-i", input_file, "-c:v", "libx264", "-preset", "fast", "crf", "22", "-s", "1280x720", "-c:a", "libfdk_aac", "-b:a", "196k", "-ar", "44100", "-pix_fmt", "yuv420p", output_file]
commands_list = []

input_file = "/path/to/input/file"
output_file = "path/to/desired/output/output_file.ext"
