import pygame
import requests
from io import BytesIO
from pydub import AudioSegment
import os

def download_audio_from_url(url):
    response = requests.get(url)
    return BytesIO(response.content)

def convert_to_wav(audio_data):
    audio = AudioSegment.from_file(audio_data)
    wav_data = BytesIO()
    audio.export(wav_data, format='wav')
    wav_data.seek(0)
    return wav_data

def play_sound(audio_data):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    pygame.quit()

def play_sound_from_url(url):
    try:
        audio_data = download_audio_from_url(url)
        wav_data = convert_to_wav(audio_data)
        play_sound(wav_data)

    except Exception as e:
        print("Error:", e)

# Example usage
url = "http://www.example.com/example_sound.mp3"  # Replace this with your URL
play_sound_from_url(url)
