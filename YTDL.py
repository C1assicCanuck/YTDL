import win32gui, win32con

win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)


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

    try:
        __import__("PyQt6")
    except ImportError:
        pip.main(['install', "PyQt6"])

dependancies()

import youtube_dl, ffmpeg, os, sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

wdir = str(os.path.dirname(__file__) + "\\")
os.chdir(wdir)

with open("uitemp.ui", "w") as ui:
    ui.write("""<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>YTDL</class>
 <widget class="QWidget" name="YTDL">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>360</width>
    <height>200</height>
   </rect>
  </property>
  <property name="palette">
   <palette>
    <active>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>170</red>
        <green>170</green>
        <blue>170</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </active>
    <inactive>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>170</red>
        <green>170</green>
        <blue>170</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </inactive>
    <disabled>
     <colorrole role="WindowText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Light">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Midlight">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Dark">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Mid">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>170</red>
        <green>170</green>
        <blue>170</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Text">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="BrightText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ButtonText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>127</red>
        <green>127</green>
        <blue>127</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Shadow">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="AlternateBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>255</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipBase">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>255</red>
        <green>255</green>
        <blue>220</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="ToolTipText">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="PlaceholderText">
      <brush brushstyle="SolidPattern">
       <color alpha="128">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </disabled>
   </palette>
  </property>
  <property name="windowTitle">
   <string>YTDL</string>
  </property>
  <property name="autoFillBackground">
   <bool>true</bool>
  </property>
  <widget class="QRadioButton" name="v480">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>40</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>480p</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="v720">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>60</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>720p</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="v1080">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>80</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>1080p</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="v1440">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>100</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>1440p</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="k4">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>120</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>4k</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="k5">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>140</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>5k</string>
   </property>
  </widget>
  <widget class="QRadioButton" name="k8">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>160</y>
     <width>82</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>8k</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="urlinp">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>341</width>
     <height>20</height>
    </rect>
   </property>
   <property name="placeholderText">
    <string notr="true">URL</string>
   </property>
  </widget>
  <widget class="QPushButton" name="ok">
   <property name="geometry">
    <rect>
     <x>270</x>
     <y>160</y>
     <width>71</width>
     <height>21</height>
    </rect>
   </property>
   <property name="palette">
    <palette>
     <active>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Light">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Midlight">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Dark">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Mid">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>170</red>
         <green>170</green>
         <blue>170</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="BrightText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ButtonText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Base">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Window">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Shadow">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="AlternateBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>220</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
     </active>
     <inactive>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Light">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Midlight">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Dark">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Mid">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>170</red>
         <green>170</green>
         <blue>170</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="BrightText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ButtonText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Base">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Window">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Shadow">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="AlternateBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>220</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
     </inactive>
     <disabled>
      <colorrole role="WindowText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Light">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Midlight">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Dark">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Mid">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>170</red>
         <green>170</green>
         <blue>170</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Text">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="BrightText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ButtonText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>127</red>
         <green>127</green>
         <blue>127</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Base">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Window">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="Shadow">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="AlternateBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>255</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipBase">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>255</red>
         <green>255</green>
         <blue>220</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="ToolTipText">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
      <colorrole role="PlaceholderText">
       <brush brushstyle="SolidPattern">
        <color alpha="128">
         <red>0</red>
         <green>0</green>
         <blue>0</blue>
        </color>
       </brush>
      </colorrole>
     </disabled>
    </palette>
   </property>
   <property name="text">
    <string>Done</string>
   </property>
   <property name="flat">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QTextEdit" name="information">
   <property name="geometry">
    <rect>
     <x>100</x>
     <y>40</y>
     <width>251</width>
     <height>111</height>
    </rect>
   </property>
   <property name="autoFillBackground">
    <bool>true</bool>
   </property>
   <property name="frameShape">
    <enum>QFrame::NoFrame</enum>
   </property>
   <property name="readOnly">
    <bool>true</bool>
   </property>
   <property name="acceptRichText">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QProgressBar" name="progressBar">
   <property name="geometry">
    <rect>
     <x>97</x>
     <y>161</y>
     <width>161</width>
     <height>20</height>
    </rect>
   </property>
   <property name="maximum">
    <number>4</number>
   </property>
   <property name="value">
    <number>0</number>
   </property>
   <property name="textVisible">
    <bool>false</bool>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>""")



class app(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("uitemp.ui", self) #change this to the one file system.
        os.remove("uitemp.ui")
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
        else:
            self.dler(URL)
    
    def ytdl(self, optV, optA, link):
        youtube_dl.YoutubeDL(optV).download([link])
        youtube_dl.YoutubeDL(optA).download([link])

    def getinfo(self, optV, optA, link):
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


    def dler(self, vlink, resH = None):
        if resH != None:
            self.optionsV = {"format" : "bestvideo[height<={}]".format(resH), "outtmpl" : r"%(id)s.%(ext)s"}
        else: 
            self.optionsV = {"format" : "bestvideo".format(resH), "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.optionsA = {"format" : "bestaudio", "outtmpl" : r"%(id)s.%(ext)s"}
        
        self.ytdl(self.optionsV, self.optionsA, vlink)
        self.progressBar.setValue(2)

        self.getinfo(self.optionsV, self.optionsA, vlink)
        self.progressBar.setValue(3)

        v = ffmpeg.input(VA[0])
        a = ffmpeg.input(VA[1])

        ff = ffmpeg.output(v, a, "{}.mp4".format(vT), vcodec='copy', acodec='aac')
        ff = ffmpeg.overwrite_output(ff)
        ff.run(cmd = str(wdir + "ffmpeg.exe"))
        os.remove(VA[0])
        os.remove(VA[1])
        self.information.setText("{}.mp4 has been saved in the location:\n{}.mp4".format(vT, wdir + vT))
        self.progressBar.setValue(4)


gui = QApplication(sys.argv)

window = app()
window.show()

gui.exec()
