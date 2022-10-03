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
Import data 
"""

# Data From parker probe as it passed the Sun 
f_S_18   = 'Sun 2018.txt'
data_S_18 = np.loadtxt(f_S_18, skiprows=2, delimiter='\t')
f_S_19   = 'Sun 2019.txt'
data_S_19 = np.loadtxt(f_S_19, skiprows=2, delimiter='\t')

# Data From parker probe as it passed Venus
f_V_18 = 'Venus 2018.txt'
data_S_18 = np.loadtxt(f_V_18, skiprows=2, delimiter='\t')
f_V_19 = 'Venus 2019.txt'
data_S_18 = np.loadtxt(f_V_19, skiprows=2, delimiter='\t')

# Data From parker probe as it passed near Mercury
f_M_19 = 'Mercury 2019.txt'
data_M_19 = np.loadtxt(f_M_19, skiprows=2, delimiter='\t')
f_M_21 = 'Mercury 2021.txt'
data_M_21 = np.loadtxt(f_M_21, skiprows=2, delimiter='\t')

# Data From parker probe as it passed near Earth
f_E_20 = 'Earth 2020.txt'
data_E_20 = np.loadtxt(f_E_20, skiprows=2, delimiter='\t')


#%%
"""
Main
"""




'''
GUI
'''
layout = [[sg.Text("Hear what Solar Weather sounds like!")], [sg.Button("Exit")]]

# Create the window
window = sg.Window("Solar Weather from Parker Solar Probe", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()

