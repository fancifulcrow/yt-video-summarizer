from pytube import YouTube
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import os

# url = input("Enter the YouTube video URL: ")
URL = "https://www.youtube.com/watch?v=rrB13utjYV4"
TEMP_FOLDER = "temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)


def get_youtube_audio(url):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        filename = 'sound.mp4'
        audio_stream.download(output_path=f"{TEMP_FOLDER}", filename=filename)
        audio = AudioSegment.from_file(f"{TEMP_FOLDER}/{filename}")

        return audio
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def transcribe_audio(audio):
    r = sr.Recognizer()

    # Break the audio into chunks of 1 minute each (60000 ms)
    chunk_length_ms = 60000
    chunks = make_chunks(audio, chunk_length_ms)

    transcript = ""

    for i, chunk in enumerate(chunks):
        chunk_filename = f"{TEMP_FOLDER}/chunk{i}.wav"
        chunk.export(chunk_filename, format="wav")
        with sr.AudioFile(chunk_filename) as source:
            audio_data = r.record(source)
            try:
                transcript += r.recognize_google(audio_data) + " "
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
        
    return transcript


def main():
    audio = get_youtube_audio(URL)
    transcript = transcribe_audio(audio)

    print(transcript)


if __name__ == "__main__":
    main()