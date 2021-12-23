from tkinter import *
from tkinter import ttk
import pafy

master = Tk()

media_option = StringVar()

audio_quality_lsit = []
audio_quality_drop_menu = StringVar()

video_quality_lsit = []
video_quality_drop_menu = StringVar()


def url():
    global data
    url = url_field.get()
    data = pafy.new(url)


def audio():
    global selected_audio
    audio_streams = data.audiostreams
    for audio_quality in audio_streams:
        audio_quality_lsit.append(audio_quality.bitrate)
    selected_audio = audio_quality_drop_menu.get()
    print("selected_audio")  # Debug Statement
    Label(master, text="Audio Bitrate: ").grid(row=7, column=1)
    show_drop_menu = OptionMenu(
        master, audio_quality_drop_menu, *audio_quality_lsit)
    show_drop_menu.grid(row=9, column=1)


def video():
    global selected_video
    video_streams = data.streams
    for video_quality in video_streams:
        video_quality_lsit.append(video_quality.resolution)
    selected_video = video_quality_drop_menu.get()
    print("selected_video")  # Debug Statement
    Label(master, text="Video Quality: ").grid(row=7, column=1)
    show_drop_menu = OptionMenu(
        master, video_quality_drop_menu, *video_quality_lsit)
    show_drop_menu.grid(row=9, column=1)


def media_select(self):
    global A_V
    A_V = media_option.get()
    if A_V == "Audio":
        audio()
    elif A_V == "Video":
        video()


def download():
    if selected_audio:
        print("Audio")  # Debug Statement
        selected_audio.download(quiet=False)
    elif selected_video:
        print("Video")  # Debug Statement
        selected_video.download(quiet=False)


Label(master, text="YouTube URL:").grid(row=0)
url_field = Entry(master)
url_field.grid(row=0, column=1)

Button(master, text='Paste URL', command=url).grid(
    row=0, column=4, sticky=W, pady=10)
Button(master, text='Download', command=download).grid(
    row=12, column=4, sticky=W, pady=10)
Label(master, text="Media Type: ").grid(row=3)

media_drop_menu = OptionMenu(
    master, media_option, "Audio", "Video", command=media_select)
media_drop_menu.grid(row=5, column=0)

mainloop()
