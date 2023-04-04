#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:36:49 2023

@author: johannes
"""

# %% Imports 

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% Classes


# %% Coordinates for domains



# %% Plots



plt.rcParams.update({'font.size':30})

fs = 25

    
# Initate figure
fig, ax = plt.subplots(figsize=(16,16))
fig.suptitle("Domains for WRF")


# Read wind turbine coordinates and find Lidar coordinates
GER = pd.read_csv("/home/johannes/Nextcloud/MA_Johannes/Data_MA/wt_coords_germanbight_v2_20210310.csv")
NL = pd.read_csv('/home/johannes/Nextcloud/MA_Johannes/Data_MA/wt_coords_gemini.csv',index_col=0)

# Read shape file
coastlines = gpd.read_file('/home/johannes/Nextcloud/MA_Johannes/Data_MA/GER.shp')
# coastlines.crs = {'init': 'epsg:4326'} # https://stackoverflow.com/questions/42751748/using-python-to-project-lat-lon-geometry-to-utm
coastlinesUTM = coastlines.to_crs(epsg=32632) # Projektion epsg:32632 ist für UTM Zone 32N in WGS84, 32U ist enthalten, da das N fuer Nord steht.

# plot all the wind farms
plt.rcParams.update({'font.size':30})
fig, ax = plt.subplots(1,1, figsize=(20,20))

ax.set_xlabel("Longitude [°]")
ax.set_ylabel("Latitude [°]")

# ax.set_ylim([53.5, 55.75])
# ax.set_xlim( [5.7, 8.7])

for wp in np.unique(GER["WF_short"]):
    
    ax.scatter(GER.loc[GER["WF_short"]==wp, "Lon_WGS84"], GER.loc[GER["WF_short"]==wp, "Lat_WGS84"],c="navy")
    
    
for wp in np.unique(NL["WF_short"]):
    
    ax.scatter(NL.loc[NL["WF_short"]==wp, "Lon_WGS84"], NL.loc[NL["WF_short"]==wp, "Lat_WGS84"],c="navy")
    
    
coastlines.plot(ax=ax, color='k', zorder=5)



# plot lidar positions(53°59'45.35"N, 6°25'14.34"E)

pos_DWG = [6.42065, 53.995930555 ]
pos_NG = [GER.loc[GER["WT_name"]=="NG17", "Lon_WGS84"], GER.loc[GER["WT_name"]=="NG17", "Lat_WGS84"]]

ax.scatter(pos_DWG[0], pos_DWG[1], c="#00FF00", marker="d", s=450)
ax.scatter(pos_NG[0], pos_NG[1], c="r", marker="d", s=450)

# ax.text(pos_DWG[0]-0.12, pos_DWG[1] - 0.05, "(2)")
# ax.text(pos_NG[0]-0.12, pos_NG[1] - 0.05, "(1)")

ax.text(6.4, 54.1, "N-2", c="navy", size=27)
ax.text(5.8, 53.95, "Gemini", c="navy", size=27)
ax.text(6.9, 53.92, "N-3", c="navy", size=27)
ax.text(7.8, 54.45, "N-4", c="navy", size=27)
ax.text(5.8, 54.22, "N-6", c="navy", size=27)
ax.text(6.41, 54.38, "N-8", c="navy", size=27)
ax.text(7.9, 53.87, "Nordergründe", c="navy", size=27)
ax.text(6.4, 53.72, "Riffgat", c="navy", size=27)

# Plot domains

ref_lat = 53.83
ref_lon = 8.17

d2_start = (67, 37)
d3_start = (67, 37)

e_we = (201,202,202)
e_sn = (111,112,112)
res = (30/3600, 30/3600, 30/3600)

dx = 18000
dy = 18000

d1 = pd.DataFrame(columns=["x", "y"])
d1_x_s = np.arange((-res[0]*e_we[0])/2, (res[0]*e_we[0])/2, res[0]) + ref_lon
d1_x_e = np.ones(111)*d1_x_s[-1]
d1_x_n = np.flip(d1_x_s)
d1_x_w = np.ones(111)*d1_x_s[0]

d1_y_e = np.arange((-res[0]*e_sn[0])/2, (res[0]*e_sn[0])/2, res[0]) + ref_lat
d1_y_s = np.ones(201)*d1_y_e[0]
d1_y_n = np.ones(201)*d1_y_e[-1]
d1_y_w = np.flip(d1_y_e)

d1["x"] = np.concatenate((d1_x_s, d1_x_e, d1_x_n, d1_x_w))
d1["y"] = np.concatenate((d1_y_s, d1_y_e, d1_y_n, d1_y_w))


plt.plot(d1["x"], d1["y"])

