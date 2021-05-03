import subprocess

## defualts
# ffmpeg = "/usr/local/bin/ffmpeg"
ffmpeg = "/Users/arthur/Desktop/ffmpeg"

def grabUserInput():

    def filterInput(message, default):
        user_input = input (message)

        if user_input == "":
            user_input = default
        return user_input

    print("Hit enter for default values\n")

    user_input_dict = {}

    user_input_dict["input_file"] = filterInput("Input File: ", "")
    user_input_dict["output_file"] = filterInput("Output File (default = ./video.mp4): ", "./video.mp4")
    user_input_dict["video_codec"] = filterInput("Video Codec (default = libx264): ", "libx264")
    user_input_dict["audio_codec"] = filterInput("Audio Codec (default = aac): ", "aac") 
    user_input_dict["audio_bitrate"] = filterInput("Audio Bitrate (default = 196k): ", "196k")
    user_input_dict["sample_rate"] = filterInput("Sample Rate (default = 44100): ", "44100")
    user_input_dict["encoding_speed"] = filterInput("Encoding Speed: (default = fast): ", "fast")
    user_input_dict["crf"] = filterInput("Constant Rate Factor: (default = 22): ", "22")
    user_input_dict["frame_size"] = filterInput("Frame Size (default = 1280x720): ", "1280x720")

    return user_input_dict

def buildFFmpegCommand():

    final_user_input = grabUserInput()

    commands_list = [
        ffmpeg,
        "-i",
        final_user_input["input_file"],
        "-c:v",
        final_user_input["video_codec"],
        "-preset",
        final_user_input["encoding_speed"],
        "-crf",
        final_user_input["crf"],
        "-s",
        final_user_input["frame_size"],
        "-c:a",
        final_user_input["audio_codec"],
        "-b:a",
        final_user_input["audio_bitrate"],
        "-ar",
        final_user_input["sample_rate"],
        "-pix_fmt",
        "yuv420p",
        final_user_input["output_file"]
        ]

    return commands_list

def runFFmpeg(commands):

    print(commands)
    if subprocess.run(commands).returncode == 0:
        print ("FFmpeg Script Ran Successfully")
    else:
        print ("There was an error running your FFmpeg script")

runFFmpeg(buildFFmpegCommand())