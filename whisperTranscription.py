import os
from moviepy.editor import VideoFileClip
import whisper
from pathlib import Path
from googletrans import Translator
import json
from datetime import datetime
from rich import print

# Define paths using pathlib
base_dir = Path(__file__).resolve().parent
files_dir = base_dir / 'files'
output_dir = base_dir / 'outputWhisper'

file_name = 'video-name'
video_path = files_dir / (file_name+'.mov')
audio_path = output_dir / (file_name+'.wav')
transcript_path = output_dir / 'transcript.txt'
transcript_with_newline_path = output_dir / (file_name+'.txt')
translated_transcript_path = output_dir / (file_name+'-translated.txt')

# Ensure output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

# Extract audio from video
def extract_audio_from_video(video_path, audio_path):
    video = VideoFileClip(str(video_path))
    video.audio.write_audiofile(str(audio_path), codec='pcm_s16le')
    video.close()

# Format the timestamp as hh:mm:ss
def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"T-{hours:02}:{minutes:02}:{seconds:02}"

# Transcribe audio using Whisper
def transcribe_audio_with_whisper(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(str(audio_path))

    full_original_text = ""
    full_original_text_with_newlines = ""

    minute_counter = 0
    minute_text = ""
    minute_text_with_newlines = ""

    for segment in result["segments"]:
        timestamp = format_timestamp(segment['start'])
        chunk_text = f"{timestamp} {segment['text']}"
        full_original_text += chunk_text + " "
        full_original_text_with_newlines += chunk_text + "\n"

        minute_text += chunk_text + " "
        minute_text_with_newlines += chunk_text + "\n"

        # Check if the current segment goes beyond the current minute
        if segment['start'] // 60 > minute_counter:
            # Write the minute transcript immediately
            minute_filename_with_newlines = output_dir / f"transcript_minute_{minute_counter:02}_with_newlines.txt"
            #with open(minute_filename_with_newlines, 'w', encoding='utf-8') as f:
            #    f.write(minute_text_with_newlines.strip())

            # Reset minute texts
            minute_text = ""
            minute_text_with_newlines = ""
            minute_counter += 1

            # Add the chunk to the new minute's texts
            minute_text += chunk_text + " "
            minute_text_with_newlines += chunk_text + "\n"

    # Write the last minute file if there is remaining text
    if minute_text:
        minute_filename_with_newlines = output_dir / f"transcript_minute_{minute_counter:02}_with_newlines.txt"
        #with open(minute_filename_with_newlines, 'w', encoding='utf-8') as f:
        #    f.write(minute_text_with_newlines.strip())

    # Write full original transcript to file
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(full_original_text.strip())

    # Write full original transcript with newlines to file
    with open(transcript_with_newline_path, 'w', encoding='utf-8') as f:
        f.write(full_original_text_with_newlines.strip())

    print("Transcription completed.")
    print("Original transcript saved to:", transcript_path)
    print("Transcript with newlines saved to:", transcript_with_newline_path)

    return full_original_text_with_newlines

def translate_to_spanish(text):
    translator = Translator()
    translated_text = ""
    text_chunks = [text[i:i+4000] for i in range(0, len(text), 4000)]  # Divide the text into chunks of 4000 characters
    for chunk in text_chunks:
        try:
            translated = translator.translate(chunk, src='en', dest='es')
            translated_text += translated.text + " "
        except Exception as e:
            print(f"Error translating chunk: {e}")
    return translated_text.strip()

def main():
    # Registrar la hora de inicio
    start_time = datetime.now()
    print(f'[bold green]Hora de inicio: {start_time.strftime("%H:%M:%S")}[/bold green]')

    # Extract audio from the video
    extract_audio_from_video(video_path, audio_path)
    
    # Transcribe the audio using Whisper
    full_original_text = transcribe_audio_with_whisper(audio_path)
    
    # Translate to Spanish
    translated_text = translate_to_spanish(full_original_text)

    # Write translated transcript to file
    with open(translated_transcript_path, 'w', encoding='utf-8') as f:
        f.write(translated_text.strip())

    print("Translated transcript saved to:", translated_transcript_path)
    
    end_time = datetime.now()
    print(f'[bold green]Hora de finalización: {end_time.strftime("%H:%M:%S")}[/bold green]')

if __name__ == "__main__":
    main()
