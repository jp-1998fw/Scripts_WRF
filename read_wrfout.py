#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:24:26 2023

@author: johannes
"""
# %% Settings

# agpath = "W://"
# homepath = "Y://"
# datapath = "Z://"

# agpath = "/home/johannes/Data_Cluster/"
# homepath ="/home/johannes/Cluster_Home/"
# datapath = "/home/johannes/Data_Personal/" 

agpath = "/nfs/group/wesys_offshore/"
homepath = "/user/need3104/"
datapath = "/nfs/data/need3104/"

# %% Imports
from netCDF4 import Dataset
import wrf 
import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap


# %% Read wrf file

# ptf = "/user/need3104/run1/"

ptf = "/gss/work/need3104/JOHANNES/WRF_XWAKES_180216/WRF_WT_on/"

# ncfile = Dataset(r"Y:\wrfout1.nc")
wrfin = Dataset(ptf + "wrfout_d03_2018-02-15_06:00:00")

# Get the WRF variables

# z = getvar(ncfile, "z")
# wspd =  getvar(ncfile, "wspd_wdir", units="kt")[0,:]
# wspd_125m = interplevel(wspd, z, 125)


# %% Plot wind speed

# Extract the wind speed data for a specific time and height level
time_index = 0 # Set the time index to the first time step
height_index = wrf.getvar(wrfin, "height_agl").argmin(dim='bottom_top') # Set the height index to the lowest level
u, v,  = wrf.getvar(wrfin, "uvmet_wspd_wdir", timeidx=time_index)
wind_speed = wrf.getvar(wrfin, "wspd_wdir", timeidx=time_index)[height_index,:]

# Create a plot of the wind speed
plt.plot(wrf.to_np(wind_speed)[:,:,5])

plt.title('Wind Speed at Time Index {} and Height Level {}'.format(time_index, height_index))
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()

# %% Try different approach 

height=120

z = wrf.getvar(wrfin, "z")
wspd =  wrf.getvar(wrfin, "wspd_wdir", units="m/s")[0,:]
wspd_interp = wrf.interplevel(wspd, z, height)



# plt.scatter(wspd_125m.XLONG, wspd_125m.XLAT, c=wspd_125m)
# plt.show()

plt.scatter(wspd_interp.XLONG, wspd_interp.XLAT, 
            c=wspd_interp)
# plt.xlim([5,10])
# plt.ylim([54.5, 55.5])
plt.colorbar()
plt.show()


