def dependancies():
    import pip

    try:
        __import__("ffmpeg")
    except ImportError:
        pip.main(['install', "ffmpeg-python"])

    try:
        __import__("youtube_dl")
    except ImportError:
        pip.main(['install', "youtube_dl"])

dependancies()

import youtube_dl
import ffmpeg
import os

os.chdir(os.getcwd())

def ytdl(optV, optA, link):
    youtube_dl.YoutubeDL(optV).download([link])
    youtube_dl.YoutubeDL(optA).download([link])

def getinfo(optV, optA, link):
    global VA, vT

    vdict = youtube_dl.YoutubeDL(optV).extract_info(link, download=False)
    vid = vdict.get("id", None)
    vext = vdict.get("ext", None)
    vtitle = vdict.get("title", None)

    adict = youtube_dl.YoutubeDL(optA).extract_info(link, download=False)
    aid = adict.get("id", None)
    aext = adict.get("ext", None)

    VA = [str(vid + "." + vext), str(aid + "." + aext)]
    vT = str(vtitle)


def dler(vlink, resH):
    optionsV = {"format" : "bestvideo[height<={}]".format(resH), "outtmpl" : r"%(id)s.%(ext)s"}
    optionsA = {"format" : "bestaudio", "outtmpl" : r"%(id)s.%(ext)s"}

    ytdl(optionsV, optionsA, vlink)

    getinfo(optionsV, optionsA, vlink)

    v = ffmpeg.input(VA[0])
    a = ffmpeg.input(VA[1])

    ff = ffmpeg.output(v, a, "{}.mp4".format(vT), vcodec='copy', acodec='aac')
    ff.run(cmd = str(os.getcwd() + r"\ffmpeg.exe"))


print("Please enter the URL of the youtube video you would like to download.")
URL = input(">>>")
resOpts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = None
while res == None or res != resOpts:
    print("\nPlease select the resolution you want.")
    print("480p(1) 720p(2) 1080p(3) 1440p(4) 4K(5) 5K(6) 8K(7)")
    res = int(input(">>>"))

    if res == 1:
        dler(URL, 480)
        break#480v
    elif res == 2:
        dler(URL, 720)
        break#720v
    elif res == 3:
        dler(URL, 1080)
        break#1080v
    elif res == 4:
        dler(URL, 1440)
        break#1440v
    elif res == 5:
        dler(URL, 2160)
        break#2160v
    elif res == 6:
        dler(URL, 2880)
        break#2880v
    elif res == 7:
        dler(URL, 4320)
        break#4320v
    else:
        print("\nThat doesnt seem to match any options, try again.")

os.remove(VA[0])
os.remove(VA[1])

print("Your video has been saved in {}".format(os.getcwd() + "\{}.mp4".format(vT)))