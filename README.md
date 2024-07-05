# YouTube Video Summarizer

## Overview
This script allows you to download audio from a YouTube video, transcribe it, and summarize the transcription. It is a practical demonstration of how to run Large Language Models (LLMs) locally on your computer.

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
pip install pytube SpeechRecognition pydub ollama
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
Here is an example of a summarization using Mistral 7b:

**Youtube Video:**
[Fireship's Linux in 100 seconds](https://www.youtube.com/watch?v=rrB13utjYV4)

**Summary:**
```
The video discusses Linux, an open-source operating system created by Linus Torvalds in 1991. Its purpose was to provide a free version of the Minix operating system, which itself was based on Unix. Today, it's widely used in web servers, embedded applications such as Smart TVs and Android mobile devices, and is considered an excellent choice for personal computers. Linux comes with various distributions (distros) like Debian, Arch, and Fedora.

The core of a Linux system includes the bootloader, kernel, and multiple subsystems like process schedulers, device drivers, and memory managers that communicate via a system call interface and C standard library. Beyond the kernel are user applications provided primarily through the Canoe project, including command-line shells, windowing systems, developer utilities, and countless other applications.

To get started with Linux, install your preferred distro, open the terminal, navigate directories using commands like `cd` and `ls`, create files using `touch`, edit them with tools like nano or emacs, view their contents with `cat`, find specific lines with `grep`, check file sizes with `du`, change owners and permissions with `chown` and `chmod`, elevate privileges with the `sudo` prefix, and install new software using package managers like APT.

The video concludes by summarizing these commands and encouraging viewers to subscribe for more content. The key takeaways are the versatility of Linux as an operating system and its extensive command-line interface, which allows users to interact with the kernel, manage files, install software, and perform various other tasks.
```

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Troubleshooting
- **FFmpeg Not Found:** Ensure FFmpeg is installed and added to your system's PATH.
- **Ollama API Issues:** Ensure Ollama is correctly set up and running on your machine.