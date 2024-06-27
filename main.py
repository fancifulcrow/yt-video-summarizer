from pytube import YouTube
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks

# url = input("Enter the YouTube video URL: ")
url = "https://www.youtube.com/watch?v=rrB13utjYV4"

yt = YouTube(url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download(output_path='.', filename='sound.mp4')

# Convert the audio to WAV format using pydub
audio = AudioSegment.from_file("sound.mp4")

r = sr.Recognizer()

# Break the audio into chunks of 1 minute each (60000 ms)
chunk_length_ms = 60000
chunks = make_chunks(audio, chunk_length_ms)

full_result = ""

for i, chunk in enumerate(chunks):
    chunk_filename = f"chunk{i}.wav"
    chunk.export(chunk_filename, format="wav")
    
    with sr.AudioFile(chunk_filename) as source:
        audio_data = r.record(source)
        try:
            result = r.recognize_google(audio_data)
            full_result += result + " "
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

print(full_result)