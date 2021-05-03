import subprocess

## defualts
ffmpeg = "/usr/local/bin/ffmpeg"


commands_list = []

## ffmpeg commands to use, commands should each be a string entered in a list, example command:
## [ffmpeg, "-i", input_file, "-c:v", "libx264", "-preset", "fast", "-crf", "22", "-s", "1280x720", "-c:a", "aac", "-b:a", "196k", "-ar", "44100", "-pix_fmt", "yuv420p", output_file]

def grabUserInput():

    def filterInput(message, default):
        user_input = input (message)

        if user_input == "":
            user_input = default

        return user_input

    print("Hit enter for default values\n")

    input_file = filterInput("Input File: ", "")
    output_file = filterInput("Output File (default = ~/Desktop): ", "~/Desktop")
    video_codec = filterInput("Video Codec (default = libx264): ", "libx264")
    audio_codec = filterInput("Audio Codec (default = aac): ", "aac") 
    audio_bitrate = filterInput("Audio Bitrate (default = 196k): ", "196k")
    sample_rate = filterInput("Sample Rate (default = 44100): ", "44100")
    encoding_speed = filterInput("Encoding Speed: (default = fast): ", "fast")
    crf = filterInput("Constant Rate Factor: (default = 22): ", "22")

# def runFFmpeg(commands):
#     if subprocess.run(commands).returncode == 0:
#         print ("FFmpeg Script Ran Successfully")
#     else:
#         print ("There was an error running your FFmpeg script")

# runFFmpeg(commands_list)

grabUserInput()