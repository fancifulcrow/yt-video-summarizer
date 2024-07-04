from pytube import YouTube
import speech_recognition as sr
from pydub import AudioSegment
from pydub.utils import make_chunks
import ollama
import os
import shutil

TEMP_FOLDER = "temp"


def get_youtube_audio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    filename = 'sound.mp4'
    audio_stream.download(output_path=TEMP_FOLDER, filename=filename)
    audio = AudioSegment.from_file(f"{TEMP_FOLDER}/{filename}")

    print("Download Complete.")

    return audio


def transcribe_audio(audio):
    print("Transcribing Audio...")
    r = sr.Recognizer()

    # Break the audio into chunks of 1 minute each (60000 ms)
    chunk_length_ms = 60000
    chunks = make_chunks(audio, chunk_length_ms)

    transcript = ""

    for i, chunk in enumerate(chunks):
        print(f"Chunk: {i + 1}/{len(chunks)}")
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

    print("Transcription complete.")
        
    return transcript


def summarize(transcript, model):
    response = ollama.chat(model=model, messages=[
        {
            'role': 'system',
            'content': 'Your goal is to summarize the text given to you in not more than 400 words. It is a transcript of a youtube video. Ensure that you get all the major points focused on in the video.'
        },
        {
            'role': 'user',
            'content': transcript,
        }
    ])

    return response['message']['content']


### For connecting to the Ollama models, you can also directly use the request module ###
# import requests

# OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"


# def summarize(transcript, model):
#     system_prompt = 'Your goal is to summarize the text given to you in not more than 400 words. It is a transcript of a youtube video. Ensure that you get all the major points focused on in the video.'

#     headers = {
#         "Content-Type" : "application/json"
#     }

#     data = {
#         "model" : model,
#         "prompt" : system_prompt + '\n\n' + transcript,
#         "stream" : False,
#         "keep_alive": "5m"
#     }

#     response = requests.post(OLLAMA_ENDPOINT, headers=headers, json=data)
#     response.raise_for_status()

#     return response.json()["response"]


def save(summary):
    with open("summary.txt", mode="w", encoding="utf-8") as file:
        file.write(summary)


def clear_temp():
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)
        os.makedirs(TEMP_FOLDER)
    else:
        os.makedirs(TEMP_FOLDER)


def main():
    clear_temp()

    url = input("Paste the Youtube Video link\n")
    audio = get_youtube_audio(url)
    transcript = transcribe_audio(audio)
    print("Now Summarizing")
    summary = summarize(transcript=transcript, model="phi3")
    
    clear_temp()

    save(summary)

    print("Summary Complete.")


if __name__ == "__main__":
    main()  