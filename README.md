# Video2Text

## Présentation

**Video2Text** est un outil Python permettant d’extraire l’audio d’une vidéo (locale ou YouTube), de le segmenter, puis de le transcrire en texte à l’aide du modèle Whisper de OpenAI. Le résultat est enregistré dans un fichier Markdown.

---

## Dépendances

```bash
pip install -r requirements.txt
```


---

## Installation & Exemples d’utilisation

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/Video2Text.git
cd Video2Text

# 2. Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate  # sous macOS/Linux
venv\Scripts\activate     # sous Windows

# 3. Mettre à jour pip et installer les dépendances Python
pip install --upgrade pip
pip install -r requirements.txt

# 4. Installer FFmpeg et yt-dlp (si non déjà présents)
#    - Sous Ubuntu/Debian :
sudo apt update && sudo apt install ffmpeg
pip install yt-dlp

# 5. Exemples d’utilisation :
#    a) Transcription d’une vidéo YouTube
python video2text.py https://www.youtube.com/watch?v=XXXXXXXXXXX

#    b) Transcription d’une vidéo locale (.mp4 ou .mkv)
#       Placez votre fichier video.mp4 dans le répertoire, puis :
python video2text.py

#    c) Transcription d’un fichier audio existant (.wav)
#       Placez audio.wav dans le répertoire, puis :
python video2text.py
