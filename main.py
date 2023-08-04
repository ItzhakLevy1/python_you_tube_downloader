import tkinter
import tkinter as tk
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get() # Grabbing what ever is in the input
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        finishLabel.configure(text="Downloaded Error", text_color="red")

# Generating and displaying the progress in numbers (%)
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_sownloaded = total_size - bytes_remaining
    pPercentage_of_complition = bytes_sownloaded / total_size * 100
    per = str(int(pPercentage_of_complition))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

# Update Progress Bar
# progressBar.set(float(pPercentage_of_complition) / 100)   # Display the progress ber filling up with blue color

# System Settings
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()   # Getting the info from within the input
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Dowlnloading indication to appear on the GUI
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progres percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

#Run app
app.mainloop()
