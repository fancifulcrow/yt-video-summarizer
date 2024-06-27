from pytube import YouTube
import speech_recognition as sr
from pydub import AudioSegment

url = input("Enter the YouTube video URL: ")

yt = YouTube(url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download(output_path='.', filename='sound.mp4')

# Convert the audio to WAV format using pydub
audio = AudioSegment.from_file("sound.mp4")
audio.export("sound.wav", format="wav")

r = sr.Recognizer()
audio = sr.AudioFile("sound.wav")