#################################################
#   Plot results for TRAPPIST-1 from VPLanet    #
# Modules used: MagmOc, AtmEsc, RadHeat, EqTide #
#################################################

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot  as plt
from time import time

plt.close('all')

clock = int(time())

# Set style for plot #
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.labelsize'] = 13
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 13
######################
cmap=plt.get_cmap('nipy_spectral')

# TRAPPIST-1 g #
data = np.loadtxt("Trappist1.g.forward")
R_N_Planet = 1.129
M_N_Planet = 1.321
Ecc = 0.002
Name_Planet = 'Trappist-1 g'
Name_Folder = 'Trappist-1_g'

time        = data[:,0]  # time (yr)
Tpot        = data[:,1]  # Potential temp magma ocean (K)
Tsurf       = data[:,2]  # Surface temp (K)
r_sol       = data[:,3]  # solidification radius (R_earth)
M_water_mo  = data[:,4] # water mass in magma ocean + atmosphere (TO)
M_water_sol = data[:,5] # water mass in solid mantle (kg)
M_O_mo      = data[:,6] # mass of oxygen in magma ocean + atmosphere (kg)
M_O_sol     = data[:,7] # mass of oxygen in solid mantle (kg)
Press_H2O   = data[:,8] # partial pressure water in atmopshere (bar)
Press_O     = data[:,9] # partial pressure oxygen in atmosphere (bar)
M_H_Space   = data[:,10] # partial pressure oxygen in atmosphere (bar)
M_O_Space   = data[:,11] # partial pressure oxygen in atmosphere (bar)
Frac_Fe2O3  = data[:,12] # partial pressure oxygen in atmosphere (bar)
NetFluxAtmo = data[:,13] # atmospheric net flux (W/m^2)
Frac_H2O    = data[:,14] # Water fraction in magma ocean
RadioHeat   = data[:,15] # Radiogenic Heating Power (TW)
TidalHeat   = data[:,16] # Tidal Heating Power (TW)
SemiMajor   = data[:,17] # Semi Major Axis (AU)
HZInnerEdge = data[:,18] # Inner Edge of the HZ (AU)

n_time = len(time)
i_end  = n_time-1

M_water_atm = np.zeros(n_time)
M_O_atm     = np.zeros(n_time)

TO        = 1.39e21         # mass of 1 Terr. Ocean [kg]
REARTH = 6.3781e6        # m
MEARTH = 5.972186e24     # kg
BIGG   = 6.67428e-11     # m**3/kg/s**2
r_p    = R_N_Planet * REARTH
m_p    = M_N_Planet * MEARTH
g      = (BIGG * m_p) / (r_p ** 2)
rho_m  = 4000

for i in range(n_time):
    M_water_atm[i] = Press_H2O[i]*1e5 * 4 * np.pi * r_p**2 / g
    M_O_atm[i]     = Press_O[i]*1e5 * 4 * np.pi * r_p**2 / g

### Plot ###

fig = plt.figure(num=None, figsize=(10, 12), dpi=300, facecolor='w', edgecolor='k')
fig.suptitle('TRAPPIST-1 g: $M^{ini}_{H_2O} = $ '+str(M_water_mo[0])+' TO', fontsize=16, fontweight='bold')

# --- Temperature --- #
ax1 = fig.add_subplot(421)
ax1.plot(time*10**-6, Tpot, label='$T_p$', color=cmap(0))
ax1.plot(time*10**-6, Tsurf, label='$T_{surf}$', linestyle='--', color=cmap(220))
ax1.legend(loc='best', frameon=True)
ax1.set_ylabel('Temperature (K)')
ax1.set_xscale('log')

# --- Solidification Radius --- #
ax2 = fig.add_subplot(422, sharex=ax1)
ax2.plot(time*10**-6, r_sol/R_N_Planet, label='$r_s$', color=cmap(0))
ax2.set_ylim([0.5,1])
ax2.set_ylabel('Solidification radius ($r_p$)')

# --- Water Mass --- #
ax3 = fig.add_subplot(423, sharex=ax1)
ax3.plot(time*10**-6, M_water_mo-M_water_atm/TO, label='magma ocean', color=cmap(0))
ax3.plot(time*10**-6, M_water_atm/TO, label='atmosphere', color=cmap(220))
ax3.plot(time*10**-6, M_water_sol, label='solid', color=cmap(70))
ax3.set_ylim([0.001*M_water_mo[0],M_water_mo[0]])
ax3.legend(loc='best', frameon=True)
ax3.set_ylabel('Water Mass (TO)')
ax3.set_yscale('log')

# --- Atmospheric pressures --- #
ax4 = fig.add_subplot(425, sharex=ax1)
ax4.plot(time*10**-6, Press_H2O, label='$H_2O$', color=cmap(0))
ax4.plot(time*10**-6, Press_O, label='$O$', color=cmap(220))
ax4.legend(loc='best', frameon=True)
ax4.set_ylabel('Atmospheric pressure (bar)')
ax4.set_yscale('log')

# --- Mass fractions magmoc --- #
ax5 = fig.add_subplot(426, sharex=ax1)
ax5.plot(time*10**-6, Frac_H2O, label='$H_2O$', color=cmap(0))
ax5.plot(time*10**-6, Frac_Fe2O3, label='$Fe_2O_3$', color=cmap(220))
ax5.legend(loc='best', frameon=True)
ax5.set_ylabel('Mass frac in magma ocean')

# --- Oxygen mass --- #
ax6 = fig.add_subplot(424, sharex=ax1)
ax6.plot(time*10**-6, M_O_mo-M_O_atm, label='magma ocean', color=cmap(0))
ax6.plot(time*10**-6, M_O_atm, label='atmosphere', color=cmap(220))
ax6.plot(time*10**-6, M_O_sol, label='solid', color=cmap(70))
ax6.legend(loc='best', frameon=True)
ax6.set_ylabel('Oxygen Mass (kg)')
ax6.set_yscale('log')
xup = max(M_O_atm[i_end],M_O_sol[i_end],M_O_mo[i_end]-M_O_atm[i_end])
ax6.set_ylim([1e-3*xup,xup])

# --- Atmosphere Net FLux --- #
ax7 = fig.add_subplot(427, sharex=ax1)
ax7.plot(time*10**-6, NetFluxAtmo, color=cmap(0))
ax7.set_ylabel('Atmospheric net flux ($W/m^2$)')
ax7.set_yscale('log')
ax7.set_xlabel('Time (Myrs)')

# --- Mantle Heating --- #
ax8 = fig.add_subplot(428, sharex=ax1)
ax8.plot(time*10**-6, RadioHeat, color=cmap(0), label='Radiogenic')
ax8.plot(time*10**-6, TidalHeat, color=cmap(220), label='Tidal')
ax8.legend(loc='best', frameon=True)
ax8.set_ylabel('Mantle Heating Power (TW)')
ax8.set_yscale('log')
ax8.set_xlabel('Time (Myrs)')


plt.subplots_adjust(left=0.1, right=0.95, top=0.93, bottom=0.05, wspace=0.25)
plt.savefig('plot.png')
