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
from wrf import (getvar, to_np, vertcross, smooth2d, CoordPair, GeoBounds,
                 get_cartopy, latlon_coords, cartopy_xlim, cartopy_ylim, interplevel)
import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
import cartopy.crs as crs
import cartopy.feature as cfeature

# %% Main

ptf = r"C:\Users\johan\Downloads\MOP1VD~T.NC"

ncfile = Dataset(r"Y:\wrfout1.nc")
ncfile2 = Dataset(r"Y:\wrfout_d03_2018-02-16_18-00-00")

# Get the WRF variables

z = getvar(ncfile, "z")
wspd =  getvar(ncfile, "wspd_wdir", units="kt")[0,:]
wspd_125m = interplevel(wspd, z, 125)

z2 = getvar(ncfile2, "z")
wspd2 =  getvar(ncfile2, "wspd_wdir", units="kt")[0,:]
wspd_125m2 = interplevel(wspd2, z2, 125)



plt.scatter(wspd_125m.XLONG, wspd_125m.XLAT, c=wspd_125m)
plt.show()

plt.scatter(wspd_125m2.XLONG, wspd_125m2.XLAT, c=wspd_125m2)
plt.show()