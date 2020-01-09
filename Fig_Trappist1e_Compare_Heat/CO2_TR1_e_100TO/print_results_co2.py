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

# TRAPPIST-1 e #
# read data
data = np.loadtxt("Trappist1.e.forward")
R_N_Planet = 0.913
M_N_Planet = 0.766
Name_Planet = 'Trappist-1 e'
Name_Folder = 'Trappist-1_e'

# write data to arrays
time        = data[:,0]  # time (yr)
Tpot        = data[:,1]  # Potential temp magma ocean (K)
Tsurf       = data[:,2]  # Surface temp (K)
r_sol       = data[:,3]  # solidification radius (R_earth)
M_water_mo  = data[:,4] # water mass in magma ocean + atmosphere (TO)
M_water_sol = data[:,5] # water mass in solid mantle (kg)
M_O_mo      = data[:,6] # mass of oxygen in magma ocean + atmosphere (kg)
M_O_sol     = data[:,7] # mass of oxygen in solid mantle (kg)
Press_H2O   = data[:,8] # pressure water in atmopshere (bar)
Press_O     = data[:,9] # pressure oxygen in atmosphere (bar)
M_H_Space   = data[:,10] # mass of hydrogen lost to space [kg]
M_O_Space   = data[:,11] # mass of oxygen lost to space [kg]
Frac_Fe2O3  = data[:,12] # Mass fraction of Fe2O3 in magma ocean
NetFluxAtmo = data[:,13] # atmospheric net flux (W/m^2)
Frac_H2O    = data[:,14] # Water fraction in magma ocean
RadioHeat   = data[:,15] # Radiogenic Heating Power (TW)
TidalHeat   = data[:,16] # Tidal Heating Power (TW)
SemiMajor   = data[:,17] # Semi Major Axis (AU)
HZInnerEdge = data[:,18] # Inner Edge of the HZ (AU)
M_CO2_mo    = data[:,19] # mass of CO2 in magma ocean + atmosphere (kg)
M_CO2_sol   = data[:,20] # mass of CO2 in solid mantle (kg)
Press_CO2   = data[:,21] # pressure CO2 in atmopshere (bar)
Frac_CO2    = data[:,22] # CO2 fraction in magma ocean

n_time = len(time)
i_end  = n_time-1

M_water_atm = np.zeros(n_time)
M_O_atm     = np.zeros(n_time)
M_CO2_atm   = np.zeros(n_time)

TO        = 1.39e21      # mass of 1 Terr. Ocean [kg]

REARTH = 6.3781e6        # m
MEARTH = 5.972186e24     # kg
BIGG   = 6.67428e-11     # m**3/kg/s**2
r_p    = R_N_Planet * REARTH
m_p    = M_N_Planet * MEARTH
g      = (BIGG * m_p) / (r_p ** 2)

man_sol   = 0 # Mantle solidified?
esc_stop  = 0 # Escape stopped? (Inner edge HZ)
atm_des   = 0 # Atmosphere desiccated?
quasi_sol = 0 # Atm desiccated & T_surf below 1000K but not solid?

# find time of solidification, desiccation, and/or entry of habitable zone
for i in range(n_time):

    M_water_atm[i] = Press_H2O[i] * 1e5 * 4 * np.pi * r_p**2 / g
    M_O_atm[i]     = Press_O[i]   * 1e5 * 4 * np.pi * r_p**2 / g
    M_CO2_atm[i]   = Press_CO2[i] * 1e5 * 4 * np.pi * r_p**2 / g

    if (atm_des == 0) and (Press_H2O[i] <= 1e-2):
        atm_des  = 1
        t_desicc = i

    if (man_sol == 0) and ((r_sol[i] >= 0.9999*R_N_Planet) or (Tpot[i]<=1660)):
        man_sol = 1
        t_solid = i

    if (esc_stop == 0) and (SemiMajor[i] >= HZInnerEdge[i]):
        esc_stop = 1
        t_habit  = i

# write results to file
results = open('Results.dat','w')
results.write('# -----------------------'+str(Name_Planet)+'----------------------- # \n')

if (atm_des == 1) and (man_sol == 0):
    results.write('# Desiccated & Solidified at same time?\n')
    results.write(str(1)+'\n')
    results.write('# Desiccation & Solidification Time [Myr]\n')
    results.write(str(time[t_desicc]*1e-6)+'\n')
    results.write('# Water mass locked in mantle [TO] \n')
    results.write(str(M_water_sol[t_desicc])+'\n')
    results.write('# Oxygen mass locked in mantle [kg] \n')
    results.write(str(M_O_sol[t_desicc])+'\n')
    results.write('# CO2 mass locked in mantle [kg] \n')
    results.write(str(M_CO2_sol[t_desicc])+'\n')
    results.write('# Total Water mass left in system [TO] \n')
    results.write(str(M_water_sol[t_desicc]+M_water_atm[t_desicc]/TO)+'\n')
    results.write('# Water pressure in atmosphere [bar] \n')
    results.write(str(Press_H2O[t_desicc])+'\n')
    results.write('# Oxygen pressure in atmosphere [bar] \n')
    results.write(str(Press_O[t_desicc])+'\n')
    results.write('# CO2 pressure in atmosphere [bar] \n')
    results.write(str(Press_CO2[t_desicc])+'\n')
    results.write('# Fe2O3 mass frac in mantle \n')
    results.write(str(Frac_Fe2O3[t_desicc])+'\n')
else:
    results.write('# Desiccated & Solidified at same time?\n')
    results.write(str(0)+'\n')
    results.write('# Solidification Time [Myr]\n')
    results.write(str(time[t_solid]*1e-6)+'\n')
    results.write('# Water mass locked in mantle [TO] \n')
    results.write(str(M_water_sol[t_solid])+'\n')
    results.write('# Oxygen mass locked in mantle [kg] \n')
    results.write(str(M_O_sol[t_solid])+'\n')
    results.write('# CO2 mass locked in mantle [kg] \n')
    results.write(str(M_CO2_sol[t_solid])+'\n')
    results.write('# Total Water mass left in system [TO] \n')
    results.write(str(M_water_sol[t_solid]+M_water_atm[t_solid]/TO)+'\n')
    results.write('# Water pressure in atmosphere [bar] \n')
    results.write(str(Press_H2O[t_solid])+'\n')
    results.write('# Oxygen pressure in atmosphere [bar] \n')
    results.write(str(Press_O[t_solid])+'\n')
    results.write('# CO2 pressure in atmosphere [bar] \n')
    results.write(str(Press_CO2[t_solid])+'\n')
    results.write('# Fe2O3 mass frac in mantle \n')
    results.write(str(Frac_Fe2O3[t_solid])+'\n')

    results.write('# ------------------------------------------------------------------ # \n')
    if (atm_des==1):
        results.write('# Atmosphere Desiccated? \n')
        results.write(str(1)+'\n')
        results.write('# Desiccation Time [Myr] \n')
        results.write(str(time[t_desicc]*1e-6)+'\n')
        results.write('# Water mass locked in mantle [TO] \n')
        results.write(str(M_water_sol[t_desicc])+'\n')
        results.write('# Total Water mass left in system [TO] \n')
        results.write(str(M_water_sol[t_desicc]+M_water_atm[t_desicc]/TO)+'\n')
        results.write('# Water pressure in atmosphere [bar] \n')
        results.write(str(Press_H2O[t_desicc])+'\n')
        results.write('# Oxygen pressure in atmosphere [bar] \n')
        results.write(str(Press_O[t_desicc])+'\n')
        results.write('# CO2 pressure in atmosphere [bar] \n')
        results.write(str(Press_CO2[t_desicc])+'\n')
    elif (esc_stop==1):
        results.write('# Atmosphere Desiccated? \n')
        results.write(str(0)+'\n')
        results.write('# Time of Habitable Zone Entry [Myr] \n')
        results.write(str(time[t_habit]*1e-6)+'\n')
        results.write('# Water mass locked in mantle [TO] \n')
        results.write(str(M_water_sol[t_habit])+'\n')
        results.write('# Total Water mass left in system [TO] \n')
        results.write(str(M_water_sol[t_habit]+M_water_atm[t_habit]/TO)+'\n')
        results.write('# Water pressure in atmosphere [bar] \n')
        results.write(str(Press_H2O[t_habit])+'\n')
        results.write('# Oxygen pressure in atmosphere [bar] \n')
        results.write(str(Press_O[t_habit])+'\n')
        results.write('# CO2 pressure in atmosphere [bar] \n')
        results.write(str(Press_CO2[t_habit])+'\n')
    else:
        results.write('# Atmosphere Desiccated? \n')
        results.write(str(0)+'\n')
        results.write('# End of Simulation [Myr] \n')
        results.write(str(time[i_end]*1e-6)+'\n')
        results.write('# Water mass locked in mantle [TO] \n')
        results.write(str(M_water_sol[i_end])+'\n')
        results.write('# Total Water mass left in system [TO] \n')
        results.write(str(M_water_sol[i_end]+M_water_atm[i_end]/TO)+'\n')
        results.write('# Water pressure in atmosphere [bar] \n')
        results.write(str(Press_H2O[i_end])+'\n')
        results.write('# Oxygen pressure in atmosphere [bar] \n')
        results.write(str(Press_O[i_end])+'\n')
        results.write('# CO2 pressure in atmosphere [bar] \n')
        results.write(str(Press_CO2[i_end])+'\n')

    results.write('# ------------------------------------------------------------------- # \n')
results.close()
