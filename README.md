# Youtube Video Downloader
A Youtube video downloader with support for downloading audio only and playlists written with pytube and customtkinter

![image](https://github.com/SouravDutta2206/Youtube-Downloader/assets/140536178/a0cd2b2e-7b9b-4023-94d7-65b6cb1f1756)



## Pre-requisites
The system should have the latest release of [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases) added to its PATH environment variables

get the latest win64-gpl.zip and extract the ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe to somewhere on the system and add this directory to the environment PATH variable in windows

## Installation
get the latest .exe file from the [releases](https://github.com/SouravDutta2206/Youtube-Downloader/releases/tag/auto)

## Usage 
After downloading the exe run it (preferebly as administrator)

in the top there is a box with text 'Output path', here the output path where the downloaded video(s) will be downloaded is to be pasted
if left black, by default the downloads will be in the C:\\users\(current user)\Downloads or simply the Downloads folder

the dropdown menus are used to set parameters for the downloads:

Link Type - Is the provided link for a video or playlist 

Data Type - Set download type to video or audio only (will download .mp3 files)

videos Resolution - Sets download videos resolution 

the box below with text "Youtube Link" is the where the Youtube link is to be pasted 

press the Download button , it will be greyed out until current download(s) is finished

the appearance mode menu is for changing app theme from light mode to dark mode or system default

## Limitations and Important Notes

![Untitled](https://github.com/SouravDutta2206/Youtube-Downloader/assets/140536178/2e8d6bcf-c81e-4ca8-945a-47b3446d4381)


with pytube downloading 60fps video is not suitable or atleast i couldn't make it work so if a video has the 1080p60 or 720p60 those streams can't be downloaded and will give you a error but regular 1080p or 720p works fine

if a stream in the resolution chosen in the menu doesn't exist then it will also give an error

The reason FFmpeg is required is because youtube stores videos and audio seperate , this is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH), so the seperate audio and videos files are needed to be post proccesed together to merge them using FFmpeg

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.





