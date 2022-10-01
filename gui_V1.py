# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:21:30 2022

@author: claye
"""

from tkinter import *
import tkinter
from PIL import Image, ImageTk, ImageOps
dir = "C:/Users/claye/Documents/GitHub/solarweather/"
root = tkinter.Tk()  # A root window for displaying objects
# open image
imgBG = Image.open(dir+'solarsystem1.png')
imgBG = imgBG.resize((512*2,256*2))
imgE = Image.open(dir+'earf.png')
imgE = imgE.rotate(4)
imgMo = Image.open(dir+'moon.png')
imgMo = imgMo.rotate(-3)

imgV = Image.open(dir+'venus.png')
imgV = ImageOps.mirror(imgV)
imgV = imgV.rotate(-4)

imgM = Image.open(dir+'mercury.png')
imgM = imgM.rotate(41)

imgBG.paste(imgE, (24*2, 128*2), imgE)
imgBG.paste(imgMo, (20*2, 110*2), imgMo)
imgBG.paste(imgV, (408*2, 128*2), imgV)
imgBG.paste(imgM, (160*2, 174*2), imgM)

# Convert the Image object into a TkPhoto object
tkimage = ImageTk.PhotoImage(imgBG)

panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)
root.title('Solar Weather')
root.mainloop()  # Start the GUI
