import customtkinter
from pytubefix import YouTube
from pytubefix import Playlist
import os
import re
from pathlib import Path
from threading import Thread 

from yt_dl import downloadVideo


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Youtube Video Downloader")
        self.geometry(f"{720}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2,3), weight=0)
        self.grid_rowconfigure(4, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=15, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Youtube", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Video", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Downloader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=0, padx=20, pady=(0, 10))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))
        
        # create main entry and button
        self.outputPath = customtkinter.CTkEntry(self, placeholder_text="Output Path")
        self.outputPath.grid(row=0, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

         # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube Link")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Download", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.button_on_click,)
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        # Create Settings menus

        self.linkTypeLabel = customtkinter.CTkLabel(self, text="Link Type")
        self.linkTypeLabel.grid(row=1, column=1, padx=20, pady=(0, 0))
        self.linkTypeOptionemenu = customtkinter.CTkOptionMenu(self, values=["Video", "Playlist"],)
        self.linkTypeOptionemenu.grid(row=2, column=1, padx=20, pady=(0, 0))

        self.dataTypeLabel = customtkinter.CTkLabel(self, text="Data Type")
        self.dataTypeLabel.grid(row=1, column=2, padx=20, pady=(0, 0))
        self.dataTypeOptionemenu = customtkinter.CTkOptionMenu(self, values=["Video", "Audio"],)
        self.dataTypeOptionemenu.grid(row=2, column=2, padx=20, pady=(0, 0))

        self.videoResLabel = customtkinter.CTkLabel(self, text="Video Resolution")
        self.videoResLabel.grid(row=1, column=3, padx=20, pady=(0, 0))
        self.videoResOptionemenu = customtkinter.CTkOptionMenu(self, values=["1080p","720p", "480p", "360p", "240p", "144p"])
        self.videoResOptionemenu.grid(row=2, column=3, padx=20, pady=(0, 0))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=4, column=1, columnspan=3 ,padx=(20, 20), pady=(20, 20), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
   

    def button_on_click(self):

        newThread = Thread(target=self.download_button_event,daemon=True)
        newThread.start()
        self.main_button_1.configure(state="disabled")
        

    def download_button_event(self):

        link = self.entry.get()
        linkType = self.linkTypeOptionemenu.get()
        dataType = self.dataTypeOptionemenu.get()
        videoResolution = self.videoResOptionemenu.get()
        outputPath = self.outputPath.get()

        if outputPath == "":
             outputPath = str(os.path.join(Path.home(), "Downloads"))
        else:
             pass

        if linkType == "Video":

            try:    
                yt = YouTube(link)
                title = yt.title
                title = re.sub("\W+"," ",title,0,re.IGNORECASE)
                self.textbox.insert("insert", f"Title: {title}" + "\n")
                downloadVideo(link,dataType,videoResolution,outputPath)
                self.textbox.insert("insert" , "\n")
                self.textbox.insert("insert" , f"Download completed"+ "\n")
                self.textbox.insert("insert" , "\n")
                self.main_button_1.configure(state="normal")  

            except:
                self.textbox.insert("insert" , "\n")
                self.textbox.insert("insert" , f"An Error has occured" + "\n")
                self.textbox.insert("insert", "\n")
                self.main_button_1.configure(state="normal")  
                return
       
        elif linkType == "Playlist":

            p = Playlist(link)

            try:
                videoCount = 1
                for video_urls in p.video_urls:
                   yt = YouTube(video_urls)
                   title = re.sub("\W+"," ",yt.title,0,re.IGNORECASE)
                   downloadVideo(video_urls,dataType,videoResolution,outputPath)
                   self.textbox.insert("insert" , "\n")
                   self.textbox.insert("insert", f"Title: {title}" + "\n")
                   self.textbox.insert("insert" , "\n")
                   self.textbox.insert("insert",f'Download Completed {videoCount} of {len(p.video_urls)}'+"\n")
                   videoCount += 1
                self.main_button_1.configure(state="normal")  
            except:
                   self.textbox.insert("insert" , "\n")
                   self.textbox.insert("insert" , f"An Error has occured")
                   self.textbox.insert("insert", "\n")
                   self.main_button_1.configure(state="normal")  
                   return
            

if __name__ == "__main__":

    app = App()
    app.mainloop()