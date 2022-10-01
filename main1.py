
print("hello butt munch")
print("Why, Hello there")
           
#%%
"""
Packages
"""
#
#
# Basic
import numpy as np
#
#
# Plot
import matplotlib as plt
#
#
# GUI
import PySimpleGUI as sg


#%%
"""
Variables
"""
#############
# Constants #
#############
#
# Speed of light
c_ls = 299792458     # In (m/s) 
#
# Planck's Constant
h_plank = 6.63*10**-34   # In (J*s)
#
# Mass of Photon
 



f =[:]
lam = [:]



#%%
"""
Import data  ?
"""
#
from spacepy import pycdf
cdf = pycdf.CDF('April 29th ISOIS.cdf')
print(cdf)
Epoch: CDF_TIME_TT2000 [60]
data: CDF_FLOAT [60]
cdf['data'][4] 
0.8609974384307861
data = cdf['data'][...] # don't forget the [...]
cdf_dat = cdf.copy()
cdf_dat.keys()
['Epoch', 'data']
cdf.close()




#%%
"""
Main
"""



E_photf = h_plank*f

E_phot = (h_plank*c_ls)/lam



'''
Audio ?
'''


import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000     #number of frames per second/frameset.      

FREQUENCY = 500     #Hz, waves per second, 261.63=C4-note.
LENGTH = 1     #seconds to play sound

BITRATE = max(BITRATE, FREQUENCY+100)

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''    

#generating wawes
for x in xrange(NUMBEROFFRAMES):
 WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

for x in xrange(RESTFRAMES): 
 WAVEDATA = WAVEDATA+chr(128)

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = BITRATE, 
                output = True)

stream.write(WAVEDATA)
stream.stop_stream()
stream.close()
p.terminate()


