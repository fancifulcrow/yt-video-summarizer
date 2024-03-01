# import streamlit as st
from openai import OpenAI

from dotenv import load_dotenv
from os import getenv

load_dotenv()

client = OpenAI(api_key=getenv("OPENAI_KEY"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)