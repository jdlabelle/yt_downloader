#!/usr/bin/env python3

import sys
import yt_dlp

URL = sys.argv[1]

# def progress_hook(d):
#     """Show ETA progress of the download"""
#     if d['status'] == 'downloading':
#         print(f"Downloading: ETA: {d['eta']}")


def extract(URL):
    """
    Download the best quality video and the best quality audio from the media
    URL. Keep the two intermediate streams; one audio-only file and one
    video-only file. Keep the final merged audio/video file and then extract
    the audio in WAV format.
    """
    ydl_opts = {
            'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                # Best Quality Audio = 0, worst = 10
                'preferredquality': 0,
                }],
            'keepvideo': True,
            'restrictfilenames': True,
            # Specify output dir paths
            'paths': {
                'home': '~/warp_storm/yt_dl/downloads',
                #'temp': '~/warp_storm/yt_dl/intermediate'
                      },
            'outtmpl': {
                'default': "%(title)s.%(ext)s",
                },
            # 'progress_hooks': [progress_hook],
            }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URL)

    return error_code


def main():
    """Run the extraction"""
    result = extract(URL)
    if result != 0:
        print('The run failed, something went wrong')
    else:
        print('The run finished successfully!')


if __name__ == "__main__":
    main()
