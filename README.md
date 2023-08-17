# Youtube Video Downloader
A Youtube video downloader with support for downloading audio only and playlists written with pytube and customtkinter

![image](https://github.com/SouravDutta2206/Youtube-Downloader/assets/140536178/a0cd2b2e-7b9b-4023-94d7-65b6cb1f1756)



## Pre-requisites
The system should have the latest release of [FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases) added to its PATH environment variable
get the latest win64-gpl.zip and extract the ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe to somewhere on the system and add this directory to the environment PATH variable in windows

There are two versions, the exe can download all videos that do not required user authentication aka age-restricted,members only videos the python script can download all videos but requires more setup
If choosing to use the basic .exe then skip the next steps and go to installation section
If choosing to use the python script then the latest release of python should be installed and and added to PATH environment variables 
Use this [article](https://www.geeksforgeeks.org/how-to-install-python-on-windows/) to properly install python first

then open a command prompt (search for cmd in windows search bar) and paste the following lines there and press enter
```
pip install customtkinter
pip install pytube
pip install git+https://github.com/nficano/pytube.git
pip install ffmpeg-python
```

## Installation
If using the .exe version get the latest YTDownloader-windowsx64.exe file from the [releases](https://github.com/SouravDutta2206/Youtube-Downloader/releases/) 

If using the python script download YTDownloader-auth.zip and extract the YTDownloader folder inside

## Usage 
For the .exe version after downloading the .exe run it (preferebly as administrator)

For the script version, assuming python is instaled properly, right click the GUI.py file and from the opened dialogue box select 'open with' then python(if python is not in the options then 'choose another app' and locate the python.exe on your system) 

the usage of GUI is explained in the GUI Explanation Section

The script version when run for the first time will prompt for the youtube authentication in the black cmd window, follow the instructions there
this is only required for the first time and then it will save the tokens.json for automatic authentication in the future downloads

### GUI Explanation
in the top there is a box with text 'Output path', here the output path where the downloaded video(s) will be downloaded is to be pasted

if left blank, by default the downloads will be in the C:\\users\\(current user)\Downloads or simply the Downloads folder

the dropdown menus are used to set parameters for the downloads:

Link Type - Is the provided link for a video or playlist 

Data Type - Set download type to video or audio only (will download .mp3 files)

videos Resolution - Sets download videos resolution 

the box below with text "Youtube Link" is the where the Youtube link is to be pasted 

press the Download button , it will be greyed out until current download(s) is finished

the appearance mode menu is for changing app theme from light mode to dark mode or system default

the script version will also open a cmd window where the authentication for the first time will happen and will output more verbose information during the downloads

## Limitations and Important Notes

![Untitled](https://github.com/SouravDutta2206/Youtube-Downloader/assets/140536178/2e8d6bcf-c81e-4ca8-945a-47b3446d4381)

with pytube downloading 60fps video is not suitable or atleast i couldn't make it work so if a video has the 1080p60 or 720p60 those streams can't be downloaded and will give you a error but regular 1080p or 720p works fine

if a stream in the resolution chosen in the menu doesn't exist then it will also give an error

the .exe can't download any videos that require youtube authentication, to get those videos the script version is needed

The reason FFmpeg is required is because youtube stores videos and audio seperate , this is a result of YouTube supporting a streaming technique called Dynamic Adaptive Streaming over HTTP (DASH), so the seperate audio and videos files are needed to be post proccesed together to merge them using FFmpeg

## Contributions

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.





