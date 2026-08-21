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

## Repository Conventions

- `.python-version` is committed on purpose to keep Python version consistent across machines.
- Generated/large media files are ignored in `.gitignore`:
	- extracted audio (for example `extracted_audio.wav`)
	- input videos (`*.mp4`, `*.mov`, `*.mkv`, `*.avi`, `*.webm`, `*.m4v`)

## Troubleshooting

- If you see `module 'whisper' has no attribute 'load_model'`, install the correct package:

```bash
uv add openai-whisper
```

