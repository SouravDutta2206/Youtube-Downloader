from pytube import YouTube
from pytube import Playlist
import os
from pathlib import Path

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

def downloadVideo(link):
    
    dataType = input("Data Type (1 for audio or 2 for video): ")

    yt = YouTube(link)

    if dataType == "2":

        yt = yt.streams.get_highest_resolution()
        yt.download(path_to_download_folder) 

    elif dataType == "1":

        yt = yt.streams.get_audio_only()
        outFile = yt.download(path_to_download_folder)
        base , ext = os.path.splitext(outFile)
        newFile = base + '.mp3'
        os.rename(outFile,newFile)

       
def main():

    linkType = input("Link Type (1 for videos, 2 for Playlist): ")

    if linkType == "1":

       link = input("Enter the YouTube video URL: ")

       try:
           downloadVideo(link)
           print("Download Completed")
       except:
           print("An Error has occured")
           return
       
    elif linkType == "2":

       link = input("Enter the Youtube Playlist URL: ")

       p = Playlist(link)

       try:
           for video_urls in p.video_urls:
               downloadVideo(video_urls)
       except:
           print("An Error has occured")
           return

main()