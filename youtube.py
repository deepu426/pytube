from pytube import YouTube

star="*"*50
print(star)
str="youtube video downloader"
print(str.center(50))
print(star)

link=input("enter video link:\n")

yt=YouTube(link)
title=yt.title

print("\n***********************{video title}*************************")
print("video title: ",title)

print("\n***********************{wait until video download}**************")
yt.streams.first().download()
print("video downloaded...")

