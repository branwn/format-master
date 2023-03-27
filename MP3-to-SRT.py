import whisper
import torch
import os
import sys
from datetime import timedelta


# Check if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

level = "base"
if len(sys.argv) == 2:
    level = sys.argv[1]
print("Using model level:", level)

# Load the Whisper model:
model = whisper.load_model(level, device=DEVICE)

def transcribe_to_srt(filename):
    # Let's get the transcript of the temporary file.
    if DEVICE == "cpu":
        transcribe = model.transcribe(filename, fp16=False)
    else:
        transcribe = model.transcribe(filename)

    results = []
    segments = transcribe['segments']
    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+',000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+',000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] is ' ' else text}\n\n"
        results.append(segment)
        
    return results



# set directory containing audios
directory = './'

# create output directory for transcription files
output_dir = os.path.join(directory, './')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)


# loop through all mp3 files in directory
for filename in os.listdir(directory):
    if filename.endswith('.mp3'):
        # open mp3 file
        mp3_file = open(os.path.join(directory, filename), 'rb')

        text = transcribe_to_srt(filename)

        # create output text file
        text_file = open(os.path.join(output_dir, filename.replace('.mp3', '.srt')), 'w')
        
        text_file.writelines(text)

        # close files
        mp3_file.close()
        text_file.close()



