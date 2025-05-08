from pytubefix import YouTube
import os
import sys
import ffmpeg
import re
import pathlib
import subprocess
import shlex


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
        # normalTitle = re.sub("\W+"," ",title,0,re.IGNORECASE)
        normalTitle = title
        # ffmpeg.concat(video,audio,v=1,a=1,).output(f'{outputPath}\{normalTitle}.mp4').run(overwrite_output=True)
        try:
                command = [
                        'ffmpeg',
                        '-threads', str(os.cpu_count()),
                        '-i', 'video.mp4',
                        '-i', 'audio.mp3',
                        '-c:v', 'copy',
                        '-c:a', 'aac',
                        '-strict', 'experimental',
                        f'{outputPath}/{normalTitle}.mp4'
                ]
                command = [shlex.quote(arg) if arg in ('video.mp4','audio.mp3',f'{outputPath}/{normalTitle}.mp4') else arg for arg in command]
                command = ' '.join(command)
                result = subprocess.run(command, capture_output=True, text=True, check=True)
                print(f"Successfully merged to {outputPath}/{normalTitle}.mp4")
                print(f"FFmpeg output:\n{result.stdout}")
        
        except subprocess.CalledProcessError as e:
                print(f"An error occurred: FFmpeg returned a non-zero exit code.")
                print(f"Return code: {e.returncode}")
                print(f"FFmpeg output (stderr):\n{e.stderr}")
        except FileNotFoundError:
                print("Error: FFmpeg is not installed or not in your system's PATH.")
        except Exception as e:
                print(f"An unexpected error occurred: {e}")
              

        os.remove("video.mp4")
        os.remove("audio.mp3")            
          

    elif dataType == "Audio":
        title = yt.title
        normalTitle = re.sub('\W+'," ",title,0,re.IGNORECASE)
        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename=f'{normalTitle}.mp3',output_path=outputPath)

if __name__ == "__main__":
    # Example usage
    link = "https://www.youtube.com/watch?v=kqvTowbg52U"
    dataType = "Video"
    videoRes = "1080p"
    outputPath = str(os.path.join(pathlib.Path.home(), "Downloads"))
    downloadVideo(link, dataType, videoRes, outputPath)

       








            
    
    