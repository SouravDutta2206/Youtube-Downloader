from pytube import YouTube
from pytube import Playlist
import os
from pathlib import Path

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

def downloadVideo(link,dataType,videoRes):
    
    yt = YouTube(link)

    if dataType == "Video":

        yt = yt.streams.get_by_resolution(videoRes)
        yt.download(path_to_download_folder)

    elif dataType == "Audio":

        yt = yt.streams.get_audio_only()
        outFile = yt.download(path_to_download_folder)
        base , ext = os.path.splitext(outFile)
        newFile = base + '.mp3'
        os.rename(outFile,newFile)

       
def downloader(link,linkType,dataType,videoRes):

    if linkType == "Video":

       try:
           downloadVideo(link,dataType,videoRes)
           print("Download Completed")
       except:
           print("An Error has occured")
           return
       
    elif linkType == "Playlist":

       p = Playlist(link)

       try:
           videoCount = 1
           for video_urls in p.video_urls:
               downloadVideo(video_urls,dataType,videoRes)
               print(f'Download Completed {videoCount} of {len(p.video_urls)}')
               videoCount += 1
       except:
           print("An Error has occured")
           return





            
    
    