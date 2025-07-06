# yt_downloader

A small program using [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download audio/video media from a site like YouTube.

## Features

- Keeps separated audio-only and video-only media files
- Creates a merged audio/video media file
- Extracts audio to a specified format (WAV)

## Purpose

Easy way to get data for deepfake research.

## Dependencies

You need the FFMPEG binary. Follow the instructions located [here](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)

```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
```
