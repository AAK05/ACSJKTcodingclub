from pytube import YouTube
import os

url = input("Please enter video URL")
yt = YouTube(url)
title = yt.title
title = title.replace(" ", "")
filename = title + ".mp4"
try:
    vidstream = yt.streams.filter(file_extension="mp4").filter(res="1080p").first()
except:
    try:
        vidstream = yt.streams.filter(file_extension="mp4").filter(res="720p").first()
    except:
        try:
            vidstream = yt.streams.filter(file_extension="mp4").filter(res="360p").first()
        except:
            pass
audiostream = yt.streams.filter(only_audio=True).first()
vidstream.download(filename="vidtemp")
audiostream.download(filename="audiotemp")
#command = r"C:\FFmpeg\bin\ffmpeg.exe -i vidtemp -i audiotemp -c:v copy -c:a aac {}".format(filename)
command = r"C:\FFmpeg\bin\ffmpeg.exe -i vidtemp -i audiotemp -c:v copy -c:a aac output.mp4"
os.system(command)
os.remove("vidtemp")
os.remove("audiotemp")