#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 15:36:06 2023

@author: johannes
"""

# %% Imports

import pandas as pd 
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt


# %% Read curves

curve_Gerald_3_6_120 = pd.read_csv("/home/johannes/Downloads/curve_Gerald.txt", engine="python", header=1, sep="\t", decimal=",")

P_3_6_120 = pd.read_csv("/home/johannes/Downloads/P_SWT-3.6-120.csv", header=None)
c_T_3_6_120 = pd.read_csv("/home/johannes/Downloads/c_T_SWT-3.6-120.csv", header=None)

P_4_130 = pd.read_csv("/home/johannes/Downloads/P_SWT-4.0-130.csv", header=None)
c_T_4_130 = pd.read_csv("/home/johannes/Downloads/c_T_SWT-4.0-130.csv", header=None)

# %% Interpolate to Other indices

curve_3_6_120 = pd.DataFrame(columns=["v [m/s]", "Pel [kW]", "ct [-]"], dtype="float64")
curve_4_130 = pd.DataFrame(columns=["v [m/s]", "Pel [kW]", "ct [-]"], dtype="float64")

curve_3_6_120["v [m/s]"] = curve_Gerald_3_6_120["v[m/s] "]
curve_4_130["v [m/s]"] = curve_Gerald_3_6_120["v[m/s] "]

cs_P1 = sp.interpolate.CubicSpline(P_3_6_120[0], P_3_6_120[1] )
cs_ct1 = sp.interpolate.CubicSpline(c_T_3_6_120[0], c_T_3_6_120[1] )

cs_P2 = sp.interpolate.CubicSpline(P_4_130.sort_values(by=0)[0], P_4_130.sort_values(by=0)[1] )
cs_ct2 = sp.interpolate.CubicSpline(c_T_4_130.sort_values(by=0)[0], c_T_4_130.sort_values(by=0)[1] )



curve_3_6_120["Pel [kW]"] = cs_P1(curve_3_6_120["v [m/s]"])*1000
curve_4_130["Pel [kW]"] = cs_P2(curve_3_6_120["v [m/s]"])*1000



curve_3_6_120["ct [-]"] = cs_ct1(curve_3_6_120["v [m/s]"])
curve_4_130["ct [-]"] = cs_ct2(curve_3_6_120["v [m/s]"])


curve_3_6_120["Pel [kW]"] = np.interp(curve_3_6_120["v [m/s]"], P_3_6_120[0], P_3_6_120[1])*1000
curve_4_130["Pel [kW]"] = np.interp(curve_4_130["v [m/s]"], P_4_130[0], P_4_130[1])*1000



curve_3_6_120["ct [-]"] = np.interp(curve_3_6_120["v [m/s]"], c_T_3_6_120[0], c_T_3_6_120[1])
curve_4_130["ct [-]"] = np.interp(curve_4_130["v [m/s]"], c_T_4_130[0], c_T_4_130[1])


curve_3_6_120.iloc[0,1:] = [0,0]
curve_4_130.iloc[0,1:] = [0,0]


# %% Plots

fig, ax = plt.subplots(2,1,figsize=(15,15), sharex=True)

ax[0].grid(visible=True)
ax[1].grid(visible=True)

ax[0].plot(curve_Gerald_3_6_120["v[m/s] "] , curve_Gerald_3_6_120["Pel [kW] "] , label="Senvion")
ax[0].plot(curve_3_6_120["v [m/s]"], curve_3_6_120["Pel [kW]"], label="Plot reversed (SWT-3.6)")
ax[0].plot(curve_4_130["v [m/s]"], curve_4_130["Pel [kW]"], label="Plot reversed (SWT-4.0)")

ax[1].plot(curve_Gerald_3_6_120["v[m/s] "] , curve_Gerald_3_6_120["ct[-]"] , label="Senvion")
ax[1].plot(curve_3_6_120["v [m/s]"], curve_3_6_120["ct [-]"], label="Plot reversed (SWT-3.6)")
ax[1].plot(curve_4_130["v [m/s]"], curve_4_130["ct [-]"], label="Plot reversed (SWT-4.0)")



ax[0].set_ylabel("P [kW]")

ax[1].set_ylabel("$C_T$ [-]")
ax[1].set_xlabel("v [m/s]")
ax[0].legend()


# %% Save for WRF

t1 = open("/home/johannes/Downloads/wind-turbine-1.tbl", "a")
t1.write("23\n")
t1.write("90. 120. 0.1 3.6\n")

t2 = open("/home/johannes/Downloads/wind-turbine-2.tbl", "a")
t2.write("23\n")
t2.write("95. 130. 0.1 4.\n")

for i in curve_3_6_120.index:
    
    t1.write(f"{curve_3_6_120.loc[i,'v [m/s]']}.\t{round(curve_3_6_120.loc[i,'Pel [kW]'], 2)}\t{round(curve_3_6_120.loc[i,'ct [-]'], 2)}\n")
    t2.write(f"{curve_4_130.loc[i,'v [m/s]']}.\t{round(curve_4_130.loc[i,'Pel [kW]'], 2)}\t{round(curve_3_6_120.loc[i,'ct [-]'], 2)}\n")


t1.close()
t2.close()


# %%% Make turbines.txt file

GER = pd.read_csv("/home/johannes/Nextcloud/MA_Johannes/Data_MA/wt_coords_germanbight_v2_20210310.csv")


DT = GER.loc[GER["WF_name"]=="DanTysk", ['Lat_WGS84', 'Lon_WGS84']]
DT["WT"] = 1
SB = GER.loc[GER["WF_name"]=="Sandbank", ['Lat_WGS84', 'Lon_WGS84']]
SB["WT"] = 2

windturbines = pd.concat([DT, SB], ignore_index=True)

windturbines.to_csv("/home/johannes/Downloads/windturbines.txt", sep=" ", header=False, index=False)
