# Video2Text

<<<<<<< HEAD
### Overview
=======
## Overview
>>>>>>> d0a5a01 (Initial commit)

**Video2Text** is a Python tool designed to extract audio from a video file (local or YouTube), segment the audio, and transcribe it to text using OpenAI's Whisper model. The result is saved in a Markdown file.

---

<<<<<<< HEAD
### Dependencies
=======
## Dependencies
>>>>>>> d0a5a01 (Initial commit)

```bash
pip install -r requirements.txt
```


<<<<<<< HEAD
### 1. Clone the repository
=======
# 1. Clone the repository
>>>>>>> d0a5a01 (Initial commit)
```bash
git clone https://github.com/your-username/Video2Text.git
cd Video2Text
```
<<<<<<< HEAD
### 2. Create and activate a virtual environment
=======
# 2. Create and activate a virtual environment
>>>>>>> d0a5a01 (Initial commit)
```bash
python3 -m venv venv
source venv/bin/activate  # on macOS/Linux
venv\Scripts\activate     # on Windows
```
<<<<<<< HEAD
### 4. Upgrade pip and install Python dependencies
=======
# 4. Upgrade pip and install Python dependencies
>>>>>>> d0a5a01 (Initial commit)
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
<<<<<<< HEAD
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
=======
# 6. Usage examples:
#    a) Transcribe a YouTube video
```bash
python video2text.py https://www.youtube.com/watch?v=XXXXXXXXXXX
```
#    b) Transcribe a local video (.mp4 or .mkv)
#       Place your video.mp4 file in the directory, then run:
```bash
python video2text.py
```
#    c) Transcribe an existing audio file (.wav)
#       Place audio.wav in the directory, then run:
```bash
python video2text.py
```
>>>>>>> d0a5a01 (Initial commit)
