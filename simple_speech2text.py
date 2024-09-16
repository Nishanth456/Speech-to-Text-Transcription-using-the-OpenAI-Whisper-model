import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline from Hugging Face Transformers
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# Define the path to the audio file that needs to be transcribed
sample = 'downloaded_audio.mp3'

# Perform speech recognition on the audio file
prediction = pipe(sample, batch_size=8)["text"]

# Print the transcribed text to the console
print(prediction)
