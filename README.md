# Whisper Tutorial

Transcribe speech from a video by first extracting audio with `ffmpeg`, then running OpenAI Whisper.

## What This Project Does

1. Takes a video file as input.
2. Extracts mono 16 kHz WAV audio from the video.
3. Transcribes the extracted audio using Whisper.

## Prerequisites

- Python `3.14` (pinned in `.python-version`)
- [uv](https://docs.astral.sh/uv/)
- `ffmpeg` installed and available in `PATH`

Check `ffmpeg`:

```bash
ffmpeg -version
```

## Setup

```bash
uv sync
```

## Run

```bash
uv run python main.py /path/to/video.mp4
```

Optional flags:

```bash
uv run python main.py /path/to/video.mp4 --audio-out extracted_audio.wav --model turbo
```

Enjoy coding, keep building, and let your ideas be heard.

