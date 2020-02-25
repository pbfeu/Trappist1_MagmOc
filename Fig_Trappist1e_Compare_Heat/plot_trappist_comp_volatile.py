import numpy as np
import matplotlib as mpl
import matplotlib.pyplot  as plt
# import seaborn as sns
#
# sns.set_style("whitegrid")
plt.close('all')

# Set style for plot #
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['axes.labelsize'] = 13
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 13
mpl.rcParams['axes.labelweight'] = 'bold'
######################


cmap=plt.get_cmap('nipy_spectral')

# Initial water mass [TO]
Water = 100


# TRAPPIST-1 e #
R_N_Planet = 0.913
M_N_Planet = 0.766
Ecc = 0.005
Name_Planet = 'Trappist-1 e'
Name_Folder = 'Trappist-1_e'
Short_Planet = 'e'


# read data
data_1 = np.loadtxt('CO2_TR1_e_100TO_sol/Trappist1.e.forward')
data_2 = np.loadtxt('CO2_TR1_e_100TO_heat/Trappist1.e.forward')

time_1        = data_1[:,0]  # time (yr)
Tpot_1        = data_1[:,1]  # Potential temp magma ocean (K)
Tsurf_1       = data_1[:,2]  # Surface temp (K)
r_sol_1       = data_1[:,3]  # solidification radius (R_earth)
M_water_mo_1  = data_1[:,4] # water mass in magma ocean + atmosphere (TO)
M_water_sol_1 = data_1[:,5] # water mass in solid mantle (kg)
M_O_mo_1      = data_1[:,6] # mass of oxygen in magma ocean + atmosphere (kg)
M_O_sol_1     = data_1[:,7] # mass of oxygen in solid mantle (kg)
Press_H2O_1   = data_1[:,8] # partial pressure water in atmopshere (bar)
Press_O_1     = data_1[:,9] # partial pressure oxygen in atmosphere (bar)
M_CO2_mo_1    = data_1[:,19] # mass of CO2 in magma ocean + atmosphere (kg)
M_CO2_sol_1   = data_1[:,20] # mass of CO2 in solid mantle (kg)
Press_CO2_1   = data_1[:,21] # pressure CO2 in atmopshere (bar)
Frac_CO2_1    = data_1[:,22] # CO2 fraction in magma ocean

time_2        = data_2[:,0]  # time (yr)
Tpot_2        = data_2[:,1]  # Potential temp magma ocean (K)
Tsurf_2       = data_2[:,2]  # Surface temp (K)
r_sol_2       = data_2[:,3]  # solidification radius (R_earth)
M_water_mo_2  = data_2[:,4] # water mass in magma ocean + atmosphere (TO)
M_water_sol_2 = data_2[:,5] # water mass in solid mantle (kg)
M_O_mo_2      = data_2[:,6] # mass of oxygen in magma ocean + atmosphere (kg)
M_O_sol_2     = data_2[:,7] # mass of oxygen in solid mantle (kg)
Press_H2O_2   = data_2[:,8] # partial pressure water in atmopshere (bar)
Press_O_2     = data_2[:,9] # partial pressure oxygen in atmosphere (bar)
M_CO2_mo_2    = data_2[:,19] # mass of CO2 in magma ocean + atmosphere (kg)
M_CO2_sol_2   = data_2[:,20] # mass of CO2 in solid mantle (kg)
Press_CO2_2   = data_2[:,21] # pressure CO2 in atmopshere (bar)
Frac_CO2_2    = data_2[:,22] # CO2 fraction in magma ocean

n_time_1 = len(time_1)
n_time_2 = len(time_2)

M_water_atm_1 = np.zeros(n_time_1)
M_O_atm_1     = np.zeros(n_time_1)
M_CO2_atm_1   = np.zeros(n_time_1)

M_water_atm_2 = np.zeros(n_time_2)
M_O_atm_2     = np.zeros(n_time_2)
M_CO2_atm_2   = np.zeros(n_time_2)

TO     = 1.39e21         # mass of 1 Terr. Ocean [kg]
REARTH = 6.3781e6        # m
MEARTH = 5.972186e24     # kg
BIGG   = 6.67428e-11     # m**3/kg/s**2
r_p    = R_N_Planet*REARTH
m_p    = M_N_Planet*MEARTH
g      = (BIGG * m_p) / (r_p ** 2)

for i in range(n_time_1):
    M_water_atm_1[i] = Press_H2O_1[i]*1e5 * 4 * np.pi * r_p**2 / g
    M_O_atm_1[i]     = Press_O_1[i]  *1e5 * 4 * np.pi * r_p**2 / g
    M_CO2_atm_1[i]   = Press_CO2_1[i]*1e5 * 4 * np.pi * r_p**2 / g

for i in range(n_time_2):
    M_water_atm_2[i] = Press_H2O_2[i]*1e5 * 4 * np.pi * r_p**2 / g
    M_O_atm_2[i]     = Press_O_2[i]  *1e5 * 4 * np.pi * r_p**2 / g
    M_CO2_atm_2[i]   = Press_CO2_2[i]*1e5 * 4 * np.pi * r_p**2 / g


### Plot ###
fig = plt.figure(num=None, figsize=(10, 8), dpi=300, facecolor='w', edgecolor='k')

fig.suptitle('Solid: $e=0.005$ & $^{40}K$ abundance of Earth\nDashed: $e=0.1$ and 1000 $\\times$ $^{40}K$ abundance', fontsize=16)

# ---------------------------------------------------------------------------- #
ax1 = fig.add_subplot(221)
ax1.plot(time_1*10**-6, Tpot_1, label='$T_p$', color=cmap(0))
ax1.plot(time_2*10**-6, Tpot_2, linestyle='--', color=cmap(0))

ax1.plot(time_1*10**-6, Tsurf_1, label='$T_{surf}$', color=cmap(220))
ax1.plot(time_2*10**-6, Tsurf_2, linestyle='--', color=cmap(220))

ax1.legend(loc='best', frameon=True)
ax1.set_ylabel('Temperature (K)')
ax1.set_xscale('log')
ax1.set_xlim([1,253])
ax1.set_ylim([1500,3500])

# ---------------------------------------------------------------------------- #
ax2 = fig.add_subplot(222, sharex=ax1)
ax2.plot(time_1*10**-6, M_water_atm_1/TO, label='atmosphere', color=cmap(0))
ax2.plot(time_1*10**-6, M_water_mo_1-M_water_atm_1/TO, label='magma ocean', color=cmap(70))
ax2.plot(time_1*10**-6, M_water_sol_1, label='solid', color=cmap(220))

ax2.plot(time_2*10**-6, M_water_atm_2/TO, linestyle='--',  color=cmap(0))
ax2.plot(time_2*10**-6, M_water_mo_2-M_water_atm_2/TO, linestyle='--', color=cmap(70))
ax2.plot(time_2*10**-6, M_water_sol_2, linestyle='--', color=cmap(220))

ax2.set_ylim([0.01,100])
ax2.legend(loc='best', frameon=True)
ax2.set_ylabel('Water Mass (TO)')
ax2.set_yscale('log')

# ---------------------------------------------------------------------------- #
ax3 = fig.add_subplot(223, sharex=ax1)
ax3.plot(time_1*10**-6, M_O_atm_1, label='atmosphere',   color=cmap(0))
ax3.plot(time_1*10**-6, M_O_mo_1-M_O_atm_1, label='magma ocean',   color=cmap(70))
ax3.plot(time_1*10**-6, M_O_sol_1, label='solid',   color=cmap(220))

ax3.plot(time_2*10**-6, M_O_atm_2,  linestyle='--',  color=cmap(0))
ax3.plot(time_2*10**-6, M_O_mo_2-M_O_atm_2,  linestyle='--', color=cmap(70))
ax3.plot(time_2*10**-6, M_O_sol_2,  linestyle='--', color=cmap(220))

ax3.set_ylim([1e18,1e22])
ax3.legend(loc='best', frameon=True)
ax3.set_xlabel('Time (Myr)')
ax3.set_ylabel('Oxygen Mass (kg)')
ax3.set_yscale('log')

# ---------------------------------------------------------------------------- #
ax7 = fig.add_subplot(224, sharex=ax1)
ax7.plot(time_1*10**-6, M_CO2_atm_1, label='atmosphere',   color=cmap(0))
ax7.plot(time_1*10**-6, M_CO2_mo_1-M_CO2_atm_1, label='magma ocean',   color=cmap(70))
ax7.plot(time_1*10**-6, M_CO2_sol_1, label='solid',   color=cmap(220))

ax7.plot(time_2*10**-6, M_CO2_atm_2,  linestyle='--',  color=cmap(0))
ax7.plot(time_2*10**-6, M_CO2_mo_2-M_CO2_atm_2,  linestyle='--', color=cmap(70))
ax7.plot(time_2*10**-6, M_CO2_sol_2,  linestyle='--', color=cmap(220))

ax7.set_ylim([1e18,1e23])
ax7.legend(loc='best', frameon=True)
ax7.set_xlabel('Time (Myr)')
ax7.set_ylabel('$CO_2$ Mass (kg)')
ax7.set_yscale('log')

plt.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.1, wspace=0.2, hspace=0.12)
plt.savefig('Plot_TR1_e_comp.png')
