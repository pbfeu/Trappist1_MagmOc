import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set_style("whitegrid")
plt.close('all')

cmap=plt.get_cmap('nipy_spectral')
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['lines.color'] = cmap(0)
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['xtick.labelsize'] = 15
mpl.rcParams['ytick.labelsize'] = 15
mpl.rcParams['legend.fontsize'] = 16
mpl.rcParams['axes.titleweight'] = 'bold'


planets = ['e','f','g']
masses  = [0.766,0.926,1.14]
M_Earth = 5.972186e24 # Earth mass [kg]
TO      = 1.39e21     # mass of 1 Terr. Ocean [kg]

Results_TR1_e = np.loadtxt("Results_Trappist1_e.txt", skiprows=2)
Results_TR1_f = np.loadtxt("Results_Trappist1_f.txt", skiprows=2)
Results_TR1_g = np.loadtxt("Results_Trappist1_g.txt", skiprows=2)

Results_TR1_e_co2 = np.loadtxt("Results_Trappist1_e_co2.txt", skiprows=2)

Results_TR1_e_heat = np.loadtxt("Results_Trappist1_e_heat.txt", skiprows=2)
Results_TR1_f_heat = np.loadtxt("Results_Trappist1_f_heat.txt", skiprows=2)
Results_TR1_g_heat = np.loadtxt("Results_Trappist1_g_heat.txt", skiprows=2)

Results_TR1_e_co2_heat = np.loadtxt("Results_Trappist1_e_co2_heat.txt", skiprows=2)

M_water = Results_TR1_e[:,0]  # Initial water mass [MO]

water_tot_e = Results_TR1_e[:,4]
water_tot_f = Results_TR1_f[:,4]
water_tot_g = Results_TR1_g[:,4]

water_tot_e_CO2 = Results_TR1_e_co2[:,4]

water_tot_e_heat = Results_TR1_e_heat[:,4]
water_tot_f_heat = Results_TR1_f_heat[:,4]
water_tot_g_heat = Results_TR1_g_heat[:,4]

water_tot_e_CO2_heat = Results_TR1_e_co2_heat[:,4]

n = len(water_tot_e)-1

water_tot_1000_e = min(1000, 10**(np.log10(water_tot_e[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_e[n])-np.log10(water_tot_e[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))
water_tot_1000_f = min(1000, 10**(np.log10(water_tot_f[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_f[n])-np.log10(water_tot_f[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))
water_tot_1000_g = min(1000, 10**(np.log10(water_tot_g[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_g[n])-np.log10(water_tot_g[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))

water_tot_1000_e_co2 = min(1000, 10**(np.log10(water_tot_e_CO2[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_e_CO2[n])-np.log10(water_tot_e_CO2[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))

n_heat = len(water_tot_e_heat)-1

water_tot_1000_e_heat = min(1000, 10**(np.log10(water_tot_e_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_e_heat[n_heat])-np.log10(water_tot_e_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))
water_tot_1000_f_heat = min(1000, 10**(np.log10(water_tot_f_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_f_heat[n_heat])-np.log10(water_tot_f_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))
water_tot_1000_g_heat = min(1000, 10**(np.log10(water_tot_g_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_g_heat[n_heat])-np.log10(water_tot_g_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))

# print(water_tot_e_CO2_heat[n_heat],M_water[n_heat],water_tot_e_CO2_heat[n_heat])
water_tot_1000_e_co2_heat = min(1000, 10**(np.log10(water_tot_e_CO2_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_e_CO2_heat[n_heat])-np.log10(water_tot_e_CO2_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))

M_water_long = np.append(M_water,1000)

water_tot_inter_e = np.zeros(n+2)
water_tot_inter_f = np.zeros(n+2)
water_tot_inter_g = np.zeros(n+2)

water_tot_inter_e_co2 = np.zeros(n+2)

water_tot_inter_e_heat = np.zeros(n_heat+2)
water_tot_inter_f_heat = np.zeros(n_heat+2)
water_tot_inter_g_heat = np.zeros(n_heat+2)

water_tot_inter_e_co2_heat = np.zeros(n_heat+2)

for i in range(n+1):
    water_tot_inter_e[i] = water_tot_e[i]
    water_tot_inter_f[i] = water_tot_f[i]
    water_tot_inter_g[i] = water_tot_g[i]

    water_tot_inter_e_co2[i] = water_tot_e_CO2[i]

for i in range(n_heat+1):
    water_tot_inter_e_heat[i] = water_tot_e_heat[i]
    water_tot_inter_f_heat[i] = water_tot_f_heat[i]
    water_tot_inter_g_heat[i] = water_tot_g_heat[i]

    water_tot_inter_e_co2_heat[i] = water_tot_e_CO2_heat[i]

water_tot_inter_e[n+1] = water_tot_1000_e
water_tot_inter_f[n+1] = water_tot_1000_f
water_tot_inter_g[n+1] = water_tot_1000_g

water_tot_inter_e_co2[n+1] = water_tot_1000_e_co2

water_tot_inter_e_heat[n_heat+1] = water_tot_1000_e_heat
water_tot_inter_f_heat[n_heat+1] = water_tot_1000_f_heat
water_tot_inter_g_heat[n_heat+1] = water_tot_1000_g_heat

water_tot_inter_e_co2_heat[n_heat+1] = water_tot_1000_e_co2_heat

### PLOT ###

fig = plt.figure(num=None, figsize=(10, 9), dpi=300, facecolor='w', edgecolor='k')
fig.suptitle('Water Content of the Trappist-1 Planets \n at end of magma ocean phase', fontsize=18, fontweight='bold')

plt.plot(M_water_long, water_tot_inter_e,      color=cmap(0), label='Reference heating')
plt.plot(M_water_long, water_tot_inter_e_heat, color=cmap(0), label='Extreme heating',    linestyle='--')
plt.plot(M_water_long, M_water_long,           color=cmap(0), label='Initial = remaining', linestyle=':')

plt.plot(M_water_long, water_tot_inter_e, color=cmap(220), label='e')
plt.plot(M_water_long, water_tot_inter_f, color=cmap(200), label='f')
plt.plot(M_water_long, water_tot_inter_g, color=cmap(60),  label='g')

plt.plot(M_water_long, water_tot_inter_e_co2, color=cmap(20), label='e + $CO_2$')

plt.plot(M_water_long, water_tot_inter_e_heat, color=cmap(220), linestyle='--')
plt.plot(M_water_long, water_tot_inter_f_heat, color=cmap(200), linestyle='--')
plt.plot(M_water_long, water_tot_inter_g_heat, color=cmap(60),  linestyle='--')

plt.plot(M_water_long, water_tot_inter_e_co2_heat, color=cmap(20),  linestyle='--')

plt.grid(color='grey', which='major', axis='y', linestyle='-')

plt.fill_betweenx([1e-2,1e3], 100, 1000, color='grey', alpha=0.2, linewidth=0.0)

plt.text(105, 4.3e-2, 'Extrapolation', fontsize=18, color='grey')


plt.legend(loc='best', frameon=True)

plt.xscale('log')
plt.yscale('log')
plt.xlim([1,1000])
plt.ylim([4e-2,1e3])

plt.xlabel('Initial Water Mass (Terrestrial Oceans, TO)', fontweight='bold')
plt.ylabel('Remaining Water Mass (Terrestrial Oceans, TO)', fontweight='bold')

plt.tick_params(axis='both', which='both', direction='in')

plt.subplots_adjust(left=0.1, right=0.98, top=0.88, bottom=0.07)#, wspace=0.23, hspace=0.1)
plt.savefig('Water_Trappist1_Interpol_Heat_co2.png')
