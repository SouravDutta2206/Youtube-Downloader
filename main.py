from pytube import YouTube

import os
import ffmpeg
import re
import pathlib


def downloadVideo(link,dataType,videoRes,outputPath):
    
    _cache_dir = pathlib.Path(__file__).parent.resolve() / '__cache__'
    _token_file = os.path.join(_cache_dir, 'tokens.json')
    if os.path.exists(_token_file):
          yt = YouTube(link)
    else:
        yt = YouTube(link,use_oauth=True,allow_oauth_cache=True)

    if dataType == "Video":
            
            # download video only
            yt.streams.filter(res=f"{videoRes}", progressive=False).first().download(filename='video.mp4')
            video = ffmpeg.input('video.mp4')
            #download audio only
            yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
            audio = ffmpeg.input('audio.mp3')
            title = yt.title
            normalTitle = re.sub("\W+"," ",title,0,re.IGNORECASE)
            ffmpeg.concat(video,audio,v=1,a=1).output(f'{outputPath}\{normalTitle}.mp4').run(overwrite_output=True)

            os.remove("video.mp4")
            os.remove("audio.mp3")            
          

    elif dataType == "Audio":
        title = yt.title
        normalTitle = re.sub('\W+'," ",title,0,re.IGNORECASE)
        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename=f'{normalTitle}.mp3',output_path=outputPath)

       






            
    
    