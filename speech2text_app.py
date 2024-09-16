import gradio as gr
import torch
from transformers import pipeline

# Initialize the speech-to-text pipeline from Hugging Face Transformers
pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# Define the function to transcribe audio
def transcribe_audio(audio_file):
    # Perform speech recognition on the audio file
    prediction = pipe(audio_file, batch_size=8)["text"]
    return prediction

# Set up the Gradio interface
iface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath"),
    outputs="text",
    title="Speech-to-Text Transcription using the OpenAI Whisper model",
    description="Upload an audio file to get its transcription. Supported formats include .mp3.",
)

# Launch the Gradio interface
iface.launch()
