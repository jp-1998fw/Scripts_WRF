#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:24:26 2023

@author: johannes
"""
# %% Settings

agpath = "W://"
homepath = "Y://"
datapath = "Z://"

# agpath = "/home/johannes/Data_Cluster/"
# homepath ="/home/johannes/Cluster_Home/"
# datapath = "/home/johannes/Data_Personal/" 

# agpath = "/nfs/group/wesys_offshore/"
# homepath = "/user/need3104/"
# datapath = "/nfs/data/need3104/"

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

os.chdir(homepath)

# ncfile = Dataset(f"wrfout_d03_2018-12-28_00-00-00_WT")
ncfile = Dataset(f"wrfout_d03_2018-12-28_2022_WT_smallerdt")
ncfile2 = Dataset(f"wrfout_d03_2018-12-28_00-00-00")

# Get the WRF variables

z = getvar(ncfile, "z")
wspd_125m = interplevel(wspd, z, 125)

z2 = getvar(ncfile2, "z")
wspd2 =  getvar(ncfile2, "wspd_wdir", units="m/s")[0,:]
wspd_125m2 = interplevel(wspd2, z2, 120)



# plt.scatter(wspd_125m.XLONG, wspd_125m.XLAT, c=wspd_125m)
# plt.show()

plt.scatter(wspd_125m.XLONG, wspd_125m.XLAT, c=wspd_125m, )
plt.xlabel("Longitude / °")
plt.ylabel("Latitude / °")

plt.colorbar()
plt.show()

plt.scatter(wspd_125m2.XLONG, wspd_125m2.XLAT, c=wspd_125m2, vmin=0, vmax=25)
plt.xlabel("Longitude / °")
plt.ylabel("Latitude / °")
plt.colorbar()
plt.show()


plt.scatter(wspd_125m2.XLONG, wspd_125m2.XLAT, c=wspd_125m2 - wspd_125m, vmin=-25, vmax=25)
plt.xlabel("Longitude / °")
plt.ylabel("Latitude / °")
plt.colorbar()
plt.show()