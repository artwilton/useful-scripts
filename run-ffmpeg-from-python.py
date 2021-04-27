## This script uses the subprocess module to run custom ffmpeg commands from a python script
## useful when you need to run complex commands and want something more flexible than a shell script

import subprocess

## replace this with path for your ffmpeg binary if you're not using homebrew on MacOS
ffmpeg = "/usr/local/bin/ffmpeg"