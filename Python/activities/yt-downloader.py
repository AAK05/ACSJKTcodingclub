from pytube import YouTube
import os

"""
Activity: Create a script which downloads youtube videos
Use any and all relevant skills and techniques learnt up to this point
Research how to do it, we haven't learnt how to do this, but go online and find out
Tips: Install pytube and checkout the pytube library documentation to see how to use it
"""

url = input("Please enter video URL") #Asks for url
yt = YouTube(url) #Creates a youtube object
title = yt.title #Get title of video
title = title.replace(" ", "_")
filename = title + ".mp4"
#This example uses adaptive streams for 1080p resolution downloads
#This is because progressive streams do not support 1080p
#However, it is entirely possible to do this exercise using progressive streams without 1080p capability
try: #Try and except blocks to see which resolution of video is available
    vidstream = yt.streams.filter(file_extension="mp4").filter(res="1080p").first() #Get videostream
except:
    try:
        vidstream = yt.streams.filter(file_extension="mp4").filter(res="720p").first()
    except:
        try:
            vidstream = yt.streams.filter(file_extension="mp4").filter(res="360p").first()
        except:
            pass
audiostream = yt.streams.filter(only_audio=True).first() #Get audiostream
vidstream.download(filename="vidtemp") #Download videostream
audiostream.download(filename="audiotemp") #Download audiostream
command = r"C:\FFmpeg\bin\ffmpeg.exe -i vidtemp -i audiotemp -c:v copy -c:a aac {}".format(filename) #Use FFmpeg to combine audio and video streams, filename vid title
#command = r"C:\FFmpeg\bin\ffmpeg.exe -i vidtemp -i audiotemp -c:v copy -c:a aac output.mp4" #Use FFmpeg to combine audio and video streams, filename output
os.system(command)
os.remove("vidtemp") #Delete temporary videostream
os.remove("audiotemp") #Delete temporary audiostream