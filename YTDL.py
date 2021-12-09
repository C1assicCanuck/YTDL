import yt_dlp as youtube_dl
import ffmpeg, os, sys, threading
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

wdir = str(os.path.dirname(__file__) + "\\")
os.chdir(wdir)
outpath = str(os.environ["USERPROFILE"] + "\\Downloads\\")

illegalc = ("""\/:*?"<>|""")
def remove(value):
    for c in illegalc:
        value = value.replace(c,"")
    return value

class app(QWidget):
    text = pyqtSignal(str)
    progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)
        self.setWindowIcon(QIcon('ico.ico'))
        self.ok.clicked.connect(self.startdl)
        self.progress.connect(self.progressBar.setValue)
        self.text.connect(self.information.setText)

    def startdl(self):
        self.text.emit("")
        t1 = threading.Thread(target = self.getdata)
        t1.start()

    def getdata(self):
        global URL
        self.progress.emit(1)
        URL = self.urlinp.text()
        if self.v480.isChecked():
            self.dler(URL, 480)
        elif self.v720.isChecked():
            self.dler(URL, 720)
        elif self.v1080.isChecked():
            self.dler(URL, 1080)
        elif self.v1440.isChecked():
            self.dler(URL, 1440)
        elif self.k4.isChecked():
            self.dler(URL, 2160)
        elif self.k5.isChecked():
            self.dler(URL, 2880)
        elif self.k8.isChecked():
            self.dler(URL, 4320)
        elif self.best.isChecked():
            self.dler(URL)
        elif self.mp3.isChecked():
            self.mp3dl(URL)
        else:
            self.dler(URL)
    
    def ytdl(self, link, optA, optV = None):
        if optV != None:
            youtube_dl.YoutubeDL(optV).download([link])
        youtube_dl.YoutubeDL(optA).download([link])

    def getinfo(self, link, optA, optV = None):
        global VA, vT
        adict = youtube_dl.YoutubeDL(optA).extract_info(link, download=False)
        aid = adict.get("channel_id", None)
        aext = adict.get("ext", None)
        if optV != None:
            vdict = youtube_dl.YoutubeDL(optV).extract_info(link, download=False)
            vid = vdict.get("id", None)
            vext = vdict.get("ext", None)
            vtitle = vdict.get("title", None)
            adict = youtube_dl.YoutubeDL(optA).extract_info(link, download=False)
            aid = adict.get("channel_id", None)
            aext = adict.get("ext", None)
            VA = [str(vid + "." + vext), str(aid + "." + aext)]
            vT = remove(str(vtitle))
        else:
            VA = str(aid + "." + aext)
            vT = remove(str(adict.get("title")))

        


    def dler(self, vlink, resH = None):
        if resH != None:
            self.optionsV = {"format" : "bestvideo[height<={}]".format(resH), "outtmpl" : r"%(id)s.%(ext)s"}
        else: 
            self.optionsV = {"format" : "bestvideo", "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.optionsA = {"format" : "bestaudio", "outtmpl" : r"%(channel_id)s.%(ext)s"}
        
        self.ytdl(vlink, self.optionsA, self.optionsV)
        self.progress.emit(2)

        self.getinfo(vlink, self.optionsA, self.optionsV)
        self.progress.emit(3)
        v = ffmpeg.input(VA[0])
        a = ffmpeg.input(VA[1])

        print(VA[0])
        print(VA[1])

        ff = ffmpeg.output(v, a, "{}.mp4".format(outpath + vT), vcodec='copy', acodec='aac')
        ff = ffmpeg.overwrite_output(ff)
        ff.run(cmd = str(wdir + "ffmpeg.exe"))
        os.remove(VA[0])
        os.remove(VA[1])
        self.text.emit("{}.mp4 has been saved in the location:\n{}.mp4".format(vT, outpath + vT))
        self.progress.emit(4)

    def mp3dl(self, vlink):
        self.optionsA = {"format" : "bestaudio", "outtmpl" : r"%(channel_id)s.%(ext)s"}
        
        self.ytdl(vlink, self.optionsA)
        self.progress.emit(2)

        self.getinfo(vlink, self.optionsA)
        self.progress.emit(3)

        a = ffmpeg.input(VA)

        ff = ffmpeg.output(a, "{}.mp3".format(outpath + vT))
        ff = ffmpeg.overwrite_output(ff)
        ff.run(cmd = str(wdir + "ffmpeg.exe"))
        os.remove(VA)
        self.text.emit("{}.mp3 has been saved in the location:\n{}.mp3".format(vT, outpath + vT))
        self.progress.emit(4)

gui = QApplication(sys.argv)

window = app()
window.show()

threading.Thread(target = gui.exec())