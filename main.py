from pytube import YouTube
from pytube import Playlist
import os
import ffmpeg
import re

def downloadVideo(link,dataType,videoRes,outputPath):
    
    yt = YouTube(link)

    if dataType == "Video":

        # download video only
        yt.streams.filter(res=f"{videoRes}", progressive=False).first().download(filename='video.mp4')
        video = ffmpeg.input('video.mp4')
        #download audio only
        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
        audio = ffmpeg.input('audio.mp3')
        title = yt.title
        normalTitle = re.sub("[^A-Za-z0-9]+"," ",title,0,re.IGNORECASE)
        ffmpeg.concat(video,audio,v=1,a=1).output(f'{outputPath}\{normalTitle}.mp4').run(overwrite_output=True)

        os.remove("video.mp4")
        os.remove("audio.mp3")

    elif dataType == "Audio":

        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename=f'{yt.title}.mp3',output_path=outputPath)

       






            
    
    