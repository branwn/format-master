import whisper
import torch
import os

# Check if NVIDIA GPU is available
torch.cuda.is_available()
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Load the Whisper model:
model = whisper.load_model("base", device=DEVICE)

def transcribe(filename):
    # Let's get the transcript of the temporary file.
    if DEVICE == "cpu":
        result = model.transcribe(filename, fp16=False)
    else:
        result = model.transcribe(filename)
    return result['text']


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

        text = transcribe(filename)

        # create output text file
        text_file = open(os.path.join(output_dir, filename.replace('.mp3', '.txt')), 'w')
        
        text_file.write(text)

        # close files
        mp3_file.close()
        text_file.close()



