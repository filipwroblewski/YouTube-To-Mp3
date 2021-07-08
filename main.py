#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import shutil

def downloadAllYtVideos(playlist_url):
    playlist = Playlist(playlist_url)
    print(f'Number of videos in playlist: {len(playlist.video_urls)}')
    for video_url in playlist.video_urls:
        yt = YouTube(video_url)
        print(yt.title)
        stream = yt.streams.filter(only_audio=True).first()
        stream.download()

def convertMp4ToMp3(mp4_file):
    mp3_file = mp4_file.replace('.mp4', '.mp3')
    audioclip = AudioFileClip(mp4_file)
    audioclip.write_audiofile(f'mp3/{mp3_file}')
    os.remove(mp4_file)

url = ''
downloadAllYtVideos(url)

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".mp4"):
             convertMp4ToMp3(file)

