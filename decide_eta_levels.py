# %% Imports

import numpy as np 
import matplotlib.pyplot as plt

# %% 

old_levels = [1.000, 0.997, 0.995, 0.992, 0.990, 0.987, 0.982, 0.978, 0.973,
                   0.967, 0.962, 0.956, 0.950, 0.944, 0.938, 0.931,
                   0.924, 0.917, 0.909, 0.901, 0.893, 0.885, 0.876,
                   0.866, 0.857, 0.847, 0.836, 0.825, 0.814, 0.802, 
                   0.790, 0.777, 0.764, 0.750, 0.736, 0.721, 0.705, 
                   0.689, 0.672, 0.654, 0.636, 0.617, 0.597, 0.576, 
                   0.554, 0.532, 0.509, 0.484, 0.459, 0.432, 0.405,
                   0.376, 0.346, 0.315, 0.283, 0.249, 0.214, 0.178, 
                   0.140, 0.100, 0.055, 0.000 ]


p_top = 5000
p0 = 1013.25
T0 = 288.15 #K
dT = 0.0065  # K/m
h_s = 8.4 #km



z = np.linspace(0, 5000, 100)

eta = lambda p_z: p_z - p_z/(p_surf-p_top)

print(p_z)

# %% Calculate z from eta_levels

def calc_z(eta_levels, p_top):



# %% calc eta_levels


p = p0*np.exp(-z/h_s)

plt.plot(p, z,)
plt.xlabel("$p$")
plt.ylabel("$z$ [m]")
plt.xscale("log")

# print(p)
print(z)

# %%
