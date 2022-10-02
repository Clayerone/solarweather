
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



E_phot = h_plank*f

E_phot = (h_plank*c_ls)/lam





