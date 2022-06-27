import tkinter as tk
from tkinter import messagebox
import os
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube
from tkinter.ttk import *
import pytube

window = tk.Tk()
window.geometry('500x250')
icon = PhotoImage(file="icon.png")
window.iconphoto(False,icon)


window.resizable(0,0)

window.title("ArviS | YouTube Video Downloader")
tk.Label(window, text ="Youtube Video Downloader", font ="arial 20 bold",bg="cyan").pack()
link = tk.StringVar()

checkmp4ormp3 = tk.IntVar()
checkmp4ormp3.set(1)

mp4check = ttk.Radiobutton(window,text="MP4 Olarak İndir",variable=checkmp4ormp3,value=1).pack()
mp3check = ttk.Radiobutton(window,text="MP3 Olarak İndir",variable=checkmp4ormp3,value=2).pack()

tk.Label(window, text ="Video Linkini Buraya Yapıştır", font ="arial 15 bold",bg="black",fg="white").pack()
link_error = ttk.Entry(window, width =70, textvariable = link).pack()

def Downloader():
    checker = checkmp4ormp3.get()
    if checker==1:
        try:
            url =YouTube(str(link.get()))
            video =url.streams.get_highest_resolution()
            dosyayolu = pathsave()   
            video.download(dosyayolu)
            messagebox.showinfo("ArviS | Youtube Video Downloader",f"{video.title}\n Yükleme Tamamlandı \n Kaydedilen Dizin: \n {dosyayolu}")
        except pytube.exceptions.RegexMatchError:
            messagebox.showerror("ArviS | Youtube Video Downloader","Hatalı Link Girdin")
        
        
        
                

    else:
        try:

            yt = YouTube(str(link.get()))
            video = yt.streams.filter(only_audio=True).first()
            downloaded_file = video.download(pathsave())
            base, ext = os.path.splitext(downloaded_file)
            new_file = base + '.mp3'
            os.rename(downloaded_file, new_file)
            messagebox.showinfo("ArviS | Youtube Video Downloader",f"{video.title}\n Yükleme Tamamlandı \n Kaydedilen Dizin: \n {downloaded_file}")
        except pytube.exceptions.RegexMatchError:
            messagebox.showerror("ArviS | Youtube Video Downloader","Hatalı Link Girdin")
        
            
        
                


def pathsave():
    return filedialog.askdirectory()


downloadbutton = ttk.Button(window,text ="Download", command =Downloader).place(x=200, y=150,height=40,width=100)
window.mainloop()