import os
import glob
import sys
import torch
import ffmpeg
import subprocess
from transformers import WhisperForConditionalGeneration, WhisperProcessor
import torchaudio

# Supported video extensions
video_extensions = ["*.mp4", "*.mkv"]
audio_path_wav = "audio.wav"
model_name = "sanchit-gandhi/whisper-large-v3"  # Model from Hugging Face

# Extract audio from video
def extract_audio(video_path, audio_path):
    (
        ffmpeg
        .input(video_path)
        .output(audio_path)
        .run(overwrite_output=True)
    )

# Download audio from YouTube
def download_audio_from_youtube(url, output_path="audio.wav"):
    command = [
        "yt-dlp",
        "-f", "bestaudio",
        "--extract-audio",
        "--audio-format", "wav",
        "--audio-quality", "0",
        "-o", output_path,
        url
    ]
    subprocess.run(command, check=True)

# Transcribe audio to text
def transcribe_audio(audio_path, model, processor, segment_duration=30):
    try:
        # Open the audio file
        audio_info = torchaudio.info(audio_path)
        original_sampling_rate = audio_info.sample_rate
        num_frames = audio_info.num_frames
        num_channels = audio_info.num_channels

        # Define the resampler
        resampler = torchaudio.transforms.Resample(
            orig_freq=original_sampling_rate, new_freq=16000
        )

        # Calculate the number of segments
        segment_frames = segment_duration * original_sampling_rate
        num_segments = num_frames // segment_frames

        transcriptions = []

        for i in range(num_segments + 1):
            start_frame = i * segment_frames
            end_frame = min((i + 1) * segment_frames, num_frames)

            if start_frame == end_frame:
                continue

            # Load segment
            segment, _ = torchaudio.load(
                audio_path, frame_offset=start_frame, num_frames=(end_frame - start_frame)
            )

            # Resample segment
            if original_sampling_rate != 16000:
                segment = resampler(segment)

            # Ensure mono audio
            if segment.size(0) > 1:
                segment = torch.mean(segment, dim=0, keepdim=True)

            print(f"Transcribing segment {i+1}/{num_segments+1}...")

            # Prepare inputs
            inputs = processor(
                segment.squeeze(0).cpu().numpy(),
                sampling_rate=16000,
                return_tensors="pt"
            ).input_features.to("cuda").half()

            # Generate transcription
            with torch.no_grad():
                predicted_ids = model.generate(inputs)
            transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
            transcriptions.append(transcription)

        return "\n\n".join(transcriptions)
    except Exception as e:
        print(f"An error occurred during transcription: {e}")
        return ""

# Save transcription to Markdown file
def save_transcription_to_markdown(text, filename="transcription.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

def main():
    if len(sys.argv) > 1:
        youtube_url = sys.argv[1]
        audio_path = "audio.wav"
        print(f"Downloading audio from YouTube URL: {youtube_url}")
        download_audio_from_youtube(youtube_url, audio_path)
    else:
        # Search for video files
        video_files = []
        for ext in video_extensions:
            video_files.extend(glob.glob(ext))

        # Search for audio files
        audio_files = glob.glob("*.wav") + glob.glob("*.wav")

        if audio_files:
            print(torchaudio.list_audio_backends())
            audio_path = audio_files[0]
            print(f"Transcription from existing audio file: {audio_path}")
        elif video_files:
            video_path = video_files[0]
            print(f"Extracting audio from video file: {video_path}")
            extract_audio(video_path, audio_path_wav)
            audio_path = audio_path_wav
        else:
            print("No audio or video files found.")
            return

    print(f"VRAM available before loading model: {torch.cuda.memory_allocated() / 1e9} GB")

    # Load the model and processor
    with torch.no_grad():
        model = WhisperForConditionalGeneration.from_pretrained(
            model_name, torch_dtype=torch.float16
        ).to("cuda")
        processor = WhisperProcessor.from_pretrained(model_name)

        print(f"VRAM used after loading model: {torch.cuda.memory_allocated() / 1e9} GB")

        # Transcribe audio
        text = transcribe_audio(audio_path, model, processor)

        print(f"VRAM used after transcription: {torch.cuda.memory_allocated() / 1e9} GB")

        # Save the transcribed text to a Markdown file
        save_transcription_to_markdown(text)

        # Display the transcribed text
        print(text)

        # Clean up
        del model
        torch.cuda.empty_cache()

if __name__ == "__main__":
    main()
