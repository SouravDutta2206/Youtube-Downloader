import customtkinter

from pytube import YouTube
from pytube import Playlist
from main import downloader
from main import downloadVideo

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{720}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0,1,2), weight=0)
        self.grid_rowconfigure(3, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Youtube", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Video", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=1, column=0, padx=20, pady=(0, 10))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Downloader", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=2, column=0, padx=20, pady=(0, 10))
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
       

         # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Youtube Link")
        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Download", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.download_button_event)
        self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
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
        self.videoResOptionemenu = customtkinter.CTkOptionMenu(self, values=["720p", "480p", "360p", "240p", "144p"])
        self.videoResOptionemenu.grid(row=2, column=3, padx=20, pady=(0, 0))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=3, column=1, columnspan=3 ,padx=(20, 20), pady=(20, 20), sticky="nsew")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def download_button_event(self):

        link = self.entry.get()

        linkType = self.linkTypeOptionemenu.get()

        dataType = self.dataTypeOptionemenu.get()

        videoResolution = self.videoResOptionemenu.get()

        if linkType == "Video":

           try:
               yt = YouTube(link)
               self.textbox.insert("insert", f"Title:{yt.title}" + "\n")
               downloadVideo(link,dataType,videoResolution)
               self.textbox.insert("insert" , "\n")
               self.textbox.insert("insert" , f"Download completed")
           except:
               self.textbox.insert("insert" , "\n")
               self.textbox.insert("insert" , f"An Error has occured")
               return
       
        elif linkType == "Playlist":

            p = Playlist(link)

            try:
                videoCount = 1
                for video_urls in p.video_urls:
                   yt = YouTube(video_urls)
                   downloadVideo(video_urls,dataType,videoResolution)
                   print(f'Download Completed {videoCount} of {len(p.video_urls)}')
                   self.textbox.insert("insert", f"Title:{yt.title}" + "\n")
                   self.textbox.insert("insert" , "\n")
                   self.textbox.insert("insert",f'Download Completed {videoCount} of {len(p.video_urls)}'+"\n")
                   self.textbox.insert("insert" , "\n")
                   videoCount += 1
            except:
                   print("An Error has occured")
                   return

if __name__ == "__main__":
    app = App()
    app.mainloop()