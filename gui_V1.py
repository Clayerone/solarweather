# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 17:21:30 2022

@author: claye
"""

from tkinter import *
import tkinter
from PIL import Image, ImageTk, ImageOps

def update():
    imgBG = Image.open(dir+'solarsystem1.png')
    imgBG = imgBG.resize((512*2,256*2))
    imgBG.paste(imgP, (slider.get(), 260), imgP)

    lab['text'] = slider.get()
    # root.after(1000, update) # run itself again after 1000 ms
    tkimage1 = ImageTk.PhotoImage(imgBG)
    canvas.itemconfig(image_container,image=tkimage1)
    
dir = "C:/Users/claye/Documents/GitHub/solarweather/"
root = tkinter.Tk()  # A root window for displaying objects
# open image
imgBG = Image.open(dir+'solarsystem1.png')
imgBG = imgBG.resize((512*2,256*2))
imgE = Image.open(dir+'earf.png')
imgE = imgE.rotate(4)
imgMo = Image.open(dir+'moon.png')
imgMo = imgMo.rotate(-3)
imgS = Image.open(dir+'sun1.png')

imgV = Image.open(dir+'venus.png')
imgV = ImageOps.mirror(imgV)
imgV = imgV.rotate(-4)

imgM = Image.open(dir+'mercury.png')
imgM = imgM.rotate(41)

imgP = Image.open(dir+'parker_solar_probe.png')
# imgP= ImageTk.PhotoImage(Image.open(dir+'parker_solar_probe.png'))


imgBG.paste(imgE, (24*2, 128*2), imgE)
imgBG.paste(imgMo, (20*2, 110*2), imgMo)
imgBG.paste(imgV, (408*2, 128*2), imgV)
imgBG.paste(imgM, (160*2, 174*2), imgM)
imgBG.paste(imgS, (490, 260), imgS)

imgBG.paste(imgP, (100, 260), imgP)

canvas= Canvas(root,width=512*2,height=256*2)
canvas.grid(row=0, column=2, sticky=E)
tkimage = ImageTk.PhotoImage(imgBG)
image_container =canvas.create_image(0,0, anchor="nw",image=tkimage)


# panel1 = Label(root, image=tkimage)
# panel1.grid(row=0, column=2, sticky=E)

lab = Label(root)
lab.grid(row=2, column=2)

slider = Scale(root, from_=0, to=200, orient=HORIZONTAL)
slider.grid(row= 1, column=2,sticky=E,padx = 100)
button= tkinter.Button(root, text="Update",
command=lambda:update())
button.grid(row=1,column=2,sticky=W,padx = 100)
root.title('Solar Weather')
root.mainloop()  # Start the GUI
