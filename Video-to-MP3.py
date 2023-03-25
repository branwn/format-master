import os
from moviepy.editor import *

def convert_video_to_audio(video_file, audio_file):
    video = VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(audio_file)

for file in os.listdir():
    if file.endswith(".mp4") or file.endswith(".avi") or file.endswith(".mkv"):
        video_file = file
        audio_file = os.path.splitext(file)[0] + ".mp3"
        convert_video_to_audio(video_file, audio_file)
