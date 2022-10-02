
print("hello butt munch")
print("Why, Hello there, General Kenobi!")
           
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


 






#%%
"""
Import data 
"""


fname = 'UTC_2018_10_06T18_08_26.txt'

data = np.loadtxt(fname, skiprows=2, delimiter='\t')
[len_data, wid_data] = np.shape(data)
t = data[:,0]

F_Hz = data[:,1]

#%%
"""
Main
"""


# Frequency to wave length
E_p = h_plank*F_Hz
lam = (h_plank*c_ls)/E_p


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



