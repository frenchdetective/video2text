# Video2Text

### Overview

**Video2Text** is a Python tool designed to extract audio from a video file (local or YouTube), segment the audio, and transcribe it to text using OpenAI's Whisper model. The result is saved in a Markdown file.

---

### Dependencies

```bash
pip install -r requirements.txt
```

### 1. Clone the repository
```bash
git clone https://github.com/frenchdetective/Video2Text.git
cd Video2Text
```
### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows
```
### 4. Upgrade pip and install Python dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Download the OpenAI Whisper model on Hugging Face

```bash
https://huggingface.co/openai/whisper-large-v3/blob/main/model.safetensors
```

### 6. Usage examples:
####    a) Transcribe a YouTube video
```bash
python video2text.py https://www.youtube.com/watch?v=XXXXXXXXXXX
```
####    b) Transcribe a local video (.mp4 or .mkv)
#####       Place your video.mp4 file in the directory, then run:
```bash
python video2text.py
```
####    c) Transcribe an existing audio file (.wav)
#####       Place audio.wav in the directory, then run:
```bash
python video2text.py
```