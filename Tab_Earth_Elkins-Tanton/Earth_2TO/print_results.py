#################################################
#   Plot results for TRAPPIST-1 from VPLanet    #
# Modules used: MagmOc, AtmEsc, RadHeat, EqTide #
#################################################

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot  as plt
import seaborn as sns
import os as os
from time import time

# Earth #
# read data
data = np.loadtxt("Solarsystem.Earth.forward")
R_N_Planet = 1.
M_N_Planet = 1.
Name_Planet = 'Earth'

# write data to arrays
time        = data[:,0]  # time (yr)
Tpot        = data[:,1]  # Potential temp magma ocean (K)
Tsurf       = data[:,2]  # Surface temp (K)
r_sol       = data[:,3]  # solidification radius (R_earth)
M_water_mo  = data[:,4] # water mass in magma ocean + atmosphere (TO)
M_water_sol = data[:,5] # water mass in solid mantle (TO)
M_O_mo      = data[:,6] # mass of oxygen in magma ocean + atmosphere (kg)
M_O_sol     = data[:,7] # mass of oxygen in solid mantle (kg)
Press_H2O   = data[:,8] # partial pressure water in atmopshere (bar)
Press_O     = data[:,9] # partial pressure oxygen in atmosphere (bar)
M_H_Space   = data[:,10] # partial pressure oxygen in atmosphere (bar)
M_O_Space   = data[:,11] # partial pressure oxygen in atmosphere (bar)
Frac_Fe2O3  = data[:,12] # partial pressure oxygen in atmosphere (bar)
NetFluxAtmo = data[:,13] # atmospheric net flux (W/m^2)
Frac_H2O    = data[:,14] # Water fraction in magma ocean

n_time = len(time)
i_end  = n_time-1
t_solid = i_end

M_water_atm = np.zeros(n_time)
M_O_atm     = np.zeros(n_time)

TO        = 1.39e21      # mass of 1 Terr. Ocean [kg]

REARTH = 6.3781e6        # m
MEARTH = 5.972186e24     # kg
BIGG   = 6.67428e-11     # m**3/kg/s**2
r_p    = R_N_Planet * REARTH
m_p    = M_N_Planet * MEARTH
g      = (BIGG * m_p) / (r_p ** 2)

MuH2O = 18
MuO2  = 32


# find time of solidification, desiccation, and/or entry of habitable zone
for i in range(n_time):

    M_water_atm[i] = Press_H2O[i] * 1e5 * 4 * np.pi * r_p**2 / g
    M_O_atm[i]     = Press_O[i]   * 1e5 * 4 * np.pi * r_p**2 / g

M_water_ini = M_water_mo[0]

M_water_mo_left = M_water_mo[t_solid] - M_water_atm[t_solid]/TO # in TO

M_water_out = M_water_ini - M_water_sol[t_solid] - M_water_mo_left # in TO

Press_tot = Press_H2O[t_solid] + Press_O[t_solid]

# write results to file
results = open('Results.dat','w')
results.write('# -----------------------'+str(Name_Planet)+'----------------------- # \n')

results.write('# Fraction of initial water mass degassed into atmosphere [%] \n')
results.write(str(100*M_water_out/M_water_ini)+'\n')

results.write('# Total pressure in atmosphere [bar] \n')
results.write(str(Press_tot)+'\n')

results.write('# Time to reach 98% solidification [Myr]\n')
results.write(str(time[t_solid]*1e-6)+'\n')

results.write('# Water content of liquid at 98% solidification [wt%] \n')
results.write(str(100*Frac_H2O[t_solid])+'\n')

results.write('# ------------------------------------------------------------------ # \n')
results.close()
