import argparse
import subprocess
from pathlib import Path

import whisper


def extract_audio_from_video(video_path: Path, audio_path: Path) -> None:
	"""Extract a mono 16 kHz WAV from a video file using ffmpeg."""
	cmd = [
		"ffmpeg",
		"-y",
		"-i",
		str(video_path),
		"-vn",
		"-acodec",
		"pcm_s16le",
		"-ar",
		"16000",
		"-ac",
		"1",
		str(audio_path),
	]
	subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main() -> None:
	parser = argparse.ArgumentParser(
		description="Extract audio from video and transcribe with Whisper."
	)
	parser.add_argument("video", help="Path to the input video file")
	parser.add_argument(
		"--audio-out",
		default="extracted_audio.wav",
		help="Path to save extracted audio (default: extracted_audio.wav)",
	)
	parser.add_argument(
		"--model",
		default="turbo",
		help="Whisper model name (default: turbo)",
	)
	args = parser.parse_args()

	video_path = Path(args.video)
	audio_path = Path(args.audio_out)

	if not video_path.exists():
		raise FileNotFoundError(f"Video file not found: {video_path}")

	extract_audio_from_video(video_path, audio_path)
	print(f"Audio extracted to: {audio_path}")

	model = whisper.load_model(args.model)
	result = model.transcribe(str(audio_path))

	print(f"Detected language: {result.get('language', 'unknown')}")
	print(result["text"])


if __name__ == "__main__":
	main()
