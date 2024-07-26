# YouTube Video Summarizer

## Overview
This script allows you to download audio from a YouTube video, transcribe it, and summarize the transcription. It is a practical demonstration of how to use Large Language Models (LLMs) locally on your computer.

## Requirements
Ensure you have the following installed on your computer:

- [Python](https://www.python.org/downloads/)
- [Ollama](https://ollama.com/)
- [FFmpeg](https://ffmpeg.org/download.html)

## Installation

After cloning the repository, install the required Python packages using pip:
```
pip install -r requirements.txt
```

Alternatively, you can install each package individually:

```
pip install pytubefix SpeechRecognition pydub ollama
```

You can customize the LLM used for summarization by changing the model parameter in the `summarize` function.

## Usage
1. Run the script `main.py`:
```
python main.py
```

2. Follow the prompts:
    - Paste the YouTube video URL when prompted.
    - The script will download the audio, transcribe it, summarize it using the Ollama API, and save the summary to `summary.txt`.
    - The temporary files used for audio processing are automatically cleared after execution.

## How it Works
1. **Download YouTube Audio:** The script downloads the audio from the provided YouTube URL.
2. **Transcribe Audio:** The audio is broken into chunks and transcribed using Google's Speech Recognition API.
3. **Summarize Transcription:** The transcription is summarized using the Ollama API.
4. **Save Summary:** The summary is saved to a file named summary.txt.

## Example
Here is an example of a summarization using Llama 3.1 8B:

**Youtube Video:**
[Master the Perfect ChatGPT Prompt Formula (in just 8 minutes)!](https://www.youtube.com/watch?v=jC4v5AS4RIM)

**Summary:**
```
Here is a concise summary of the text (within 400 words):

The speaker, who has spent hundreds of hours learning prompt engineering, shares the six building blocks that make up a good prompt to consistently generate high-quality outputs from AI models. The six components are: Task, Context, Exemplars, Persona, Format, and Tone.

The speaker emphasizes the importance of knowing not only what these components are but also their order of priority. They use a simple example, "I'm a 70 kg male; give me a 3-month training program," to illustrate how including relevant context is crucial for meaningful output. The speaker suggests that if you just input the task without context, there will still be some output, but with context, the output will be more relevant.

The speaker breaks down each component:

* Task: Start with an action verb and clearly articulate the end goal.
* Context: Include relevant background information to constrain endless possibilities. Ask yourself what's the user's background, what does success look like, and what environment are they in?
* Exemplars: Use examples within the prompt to improve output quality. This can be a simple example or a framework.
* Persona: Identify who you want the AI model to be and use that persona in your prompt.
* Format: Use relevant formats such as paragraphs, bullet points, or code blocks.
* Tone: Use a casual or formal tone of voice, depending on the context.

The speaker uses examples to illustrate each component and emphasizes the importance of including just enough information to get a good result. They also suggest that not all components are necessary for every prompt, but including relevant information will improve output quality.

Overall, the speaker provides a comprehensive overview of the six building blocks of a good prompt and how to use them effectively to generate high-quality outputs from AI models.
```

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Troubleshooting
- **FFmpeg Not Found:** Ensure FFmpeg is installed and added to your system's PATH.
- **Ollama API Issues:** Ensure Ollama is correctly set up and running on your machine.