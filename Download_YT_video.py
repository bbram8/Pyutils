# pip install pytube before running this 
from tkinter import messagebox as mb
from pytube import YouTube

def download(yturl, directory_to_save_to, filename_to_save):

    video_url = yturl.get()
    path_save = directory_to_save_to.get()
    file_name = filename_to_save.get()

    try:
        youtube_video = YouTube(video_url)
        video = youtube_video.streams.first()
        video.download(path_save, file_name)

    except:
        mb.showerror("Error connecting to YouTube")
    

def reset_input(right_strvar, left_strvar, function_strvar):
    right_strvar = ''
    left_strvar = ''
    function_strvar = ''
