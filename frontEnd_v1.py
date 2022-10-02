# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 23:44:32 2022

@author: claye
"""

from tkinter import *
import tkinter
from PIL import Image, ImageTk, ImageOps
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import simpleaudio as sa
from scipy import signal


####################################################################
######## this function will be replaced with the "back end" ######## 
def sinGen(a=1):
           
    frequency = 440  # Our played sig will be 440 Hz
    fs = 44100 # 44100 samples per second
    seconds = 3  # sig duration of 3 seconds
    
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)
    
    # Generate a 440 Hz sine wave
    sig = np.sin(frequency * t * 2 * np.pi)*a
    # sig = sig0*0
    # for n in range(len(t)):
    #     if sig0[n] >= 0:
    #         sig[n] = 1
    #     else:
    #         sig[n] = -0
    
    # sig = signal.sawtooth(frequency * t * 2 * np.pi)
    T0 = round(fs/frequency)+1
    return sig, T0, fs
######## this function will be replaced with the "back end" ######## 
####################################################################



def playAudio(sig,fs):
    # Ensure that highest value is in 16-bit range
    audio = sig * (2**15 - 1) / np.max(np.abs(sig))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    
    # Wait for playback to finish before exiting
    play_obj.wait_done()
    


def drawIm(x):
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

    imgP= Image.open(dir+'parker_solar_probe.png')
    imgP = ImageOps.mirror(imgP)
    imgBG.paste(imgE, (24*2, 128*2), imgE)
    imgBG.paste(imgMo, (20*2, 110*2), imgMo)
    imgBG.paste(imgV, (408*2, 128*2), imgV)
    imgBG.paste(imgM, (160*2, 174*2), imgM)
    imgBG.paste(imgS, (490, 260), imgS)
    imgBG.paste(imgP, (70+x, 260), imgP)
    tkimage = ImageTk.PhotoImage(imgBG)
    return tkimage    
    
def update():
    root.after(200,update)
    lab['text'] = str(np.round(slider.get()/400,2))+" Astronomical Units (AU) from Earth"
    tkimage = drawIm(slider.get())
    panel1.configure(image=tkimage)
    panel1.image = tkimage   
    sig, T0, fs = sinGen(1-slider.get()/400.001)
    plot(sig,T0)    
    # playAudio(sig,fs)
    # plot function is created for 
    # plotting the graph in 
    # tkinter window
    
     
def plot(sig,T0):
  
    # the figure that will contain the plot
    fig = Figure(figsize = (11, 4),
                 dpi = 100)
  
    # adding the subplot
    plot1 = fig.add_subplot(111)
  
    # plotting the graph
    plot1.plot(sig[0:T0])
  
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = root)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=3, column=2)
  
    
dir = "C:/Users/claye/Documents/GitHub/solarweather/"
root = tkinter.Tk()  # A root window for displaying objects



tkimage = drawIm(100)
panel1 = Label(root, image=tkimage)
panel1.grid(row=0, column=2, sticky=E)


panel1.grid(row=0, column=2, sticky=E)

lab = Label(root,font=("Arial",20))
lab.grid(row=2, column=2)

slider = Scale(root, from_=0, to=400, orient=HORIZONTAL,showvalue=0,
               length=400, )
slider.grid(row= 1, column=2,sticky=N,padx = 100)
button= tkinter.Button(root, text="Hear it!",
command=lambda:playAudio(sig,fs))
button.grid(row=1,column=2,sticky=W,padx = 100)

sig, T0, fs = sinGen()
plot(sig,T0)
# playAudio(sig,fs)
root.title('Solar Weather')
update()
root.mainloop()  # Start the GUI
