import youtube_dl, ffmpeg, os, sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from PyQt6 import uic

wdir = str(os.path.dirname(__file__) + "\\")
os.chdir(wdir)
outpath = str(os.environ["USERPROFILE"] + "\\Downloads\\")

class app(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui.ui", self)
        self.setWindowIcon(QIcon('ico.ico'))
        self.ok.clicked.connect(self.getdata)

    def getdata(self):
        global URL
        self.progressBar.setValue(1)
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
        aid = adict.get("id", None)
        aext = adict.get("ext", None)
        if optV != None:
            vdict = youtube_dl.YoutubeDL(optV).extract_info(link, download=False)
            vid = vdict.get("id", None)
            vext = vdict.get("ext", None)
            vtitle = vdict.get("title", None)
            adict = youtube_dl.YoutubeDL(optA).extract_info(link, download=False)
            aid = adict.get("id", None)
            aext = adict.get("ext", None)
            VA = [str(vid + "." + vext), str(aid + "." + aext)]
            vT = str(vtitle)
        else:
            VA = str(aid + "." + aext)
            vT = str(adict.get("title"))

        


    def dler(self, vlink, resH = None):
        if resH != None:
            self.optionsV = {"format" : "bestvideo[height<={}]".format(resH), "outtmpl" : r"%(id)s.%(ext)s"}
        else: 
            self.optionsV = {"format" : "bestvideo", "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.optionsA = {"format" : "bestaudio", "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.ytdl(vlink, self.optionsA, self.optionsV)
        self.progressBar.setValue(2)

        self.getinfo(vlink, self.optionsA, self.optionsV)
        self.progressBar.setValue(3)

        v = ffmpeg.input(VA[0])
        a = ffmpeg.input(VA[1])

        ff = ffmpeg.output(v, a, "{}.mp4".format(outpath + vT), vcodec='copy', acodec='aac')
        ff = ffmpeg.overwrite_output(ff)
        ff.run(cmd = str(wdir + "ffmpeg.exe"))
        os.remove(VA[0])
        os.remove(VA[1])
        self.information.setText("{}.mp4 has been saved in the location:\n{}.mp4".format(vT, outpath + vT))
        self.progressBar.setValue(4)

    def mp3dl(self, vlink):
        self.optionsA = {"format" : "bestaudio", "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.ytdl(vlink, self.optionsA)
        self.progressBar.setValue(2)

        self.getinfo(vlink, self.optionsA)
        self.progressBar.setValue(3)

        a = ffmpeg.input(VA)

        ff = ffmpeg.output(a, "{}.mp3".format(outpath + vT))
        ff = ffmpeg.overwrite_output(ff)
        ff.run(cmd = str(wdir + "ffmpeg.exe"))
        os.remove(VA)
        self.information.setText("{}.mp3 has been saved in the location:\n{}.mp3".format(vT, outpath + vT))
        self.progressBar.setValue(4)

gui = QApplication(sys.argv)

window = app()
window.show()

gui.exec()