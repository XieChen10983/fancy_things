# coding=gbk
from moviepy.editor import *

video_path = r'D:\qq�����ļ�\928978561\FileRecv\MobileFile\Taylor Swift - Look What You Made Me Do_k00242mjc.mp4'
audio_path = r'F:\����\Taylor_Swift_look_what_you_make_me_do.mp3'
video = VideoFileClip(filename=video_path)
audio = video.audio
audio.write_audiofile(audio_path)
