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
masses  = np.array([0.766,0.926,1.14])
M_Earth = 5.972186e24 # Earth mass [kg]
TO      = 1.39e21     # mass of 1 Terr. Ocean [kg]

factor  = TO / (M_Earth * masses)
print(factor)

Results_TR1_e = np.loadtxt("Results_Trappist1_e.txt", skiprows=2)
Results_TR1_f = np.loadtxt("Results_Trappist1_f.txt", skiprows=2)
Results_TR1_g = np.loadtxt("Results_Trappist1_g.txt", skiprows=2)

Results_TR1_e_heat = np.loadtxt("Results_Trappist1_e_heat.txt", skiprows=2)
Results_TR1_f_heat = np.loadtxt("Results_Trappist1_f_heat.txt", skiprows=2)
Results_TR1_g_heat = np.loadtxt("Results_Trappist1_g_heat.txt", skiprows=2)

M_water = Results_TR1_e[:,0]  # Initial water mass [MO]

water_tot_e = Results_TR1_e[:,4]
water_tot_f = Results_TR1_f[:,4]
water_tot_g = Results_TR1_g[:,4]

water_tot_e_heat = Results_TR1_e_heat[:,4]
water_tot_f_heat = Results_TR1_f_heat[:,4]
water_tot_g_heat = Results_TR1_g_heat[:,4]

n = len(water_tot_e)-1

water_tot_1000_e = min(1000, 10**(np.log10(water_tot_e[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_e[n])-np.log10(water_tot_e[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))
water_tot_1000_f = min(1000, 10**(np.log10(water_tot_f[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_f[n])-np.log10(water_tot_f[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))
water_tot_1000_g = min(1000, 10**(np.log10(water_tot_g[n]) + (3-np.log10(M_water[n])) * (np.log10(water_tot_g[n])-np.log10(water_tot_g[n-1]))/(np.log10(M_water[n])-np.log10(M_water[n-1]))))

n_heat = len(water_tot_e_heat)-1

water_tot_1000_e_heat = min(1000, 10**(np.log10(water_tot_e_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_e_heat[n_heat])-np.log10(water_tot_e_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))
water_tot_1000_f_heat = min(1000, 10**(np.log10(water_tot_f_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_f_heat[n_heat])-np.log10(water_tot_f_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))
water_tot_1000_g_heat = min(1000, 10**(np.log10(water_tot_g_heat[n_heat]) + (3-np.log10(M_water[n_heat])) * (np.log10(water_tot_g_heat[n_heat])-np.log10(water_tot_g_heat[n_heat-1]))/(np.log10(M_water[n_heat])-np.log10(M_water[n_heat-1]))))

M_water_long = np.append(M_water,1000)

water_tot_inter_e = np.zeros(n+2)
water_tot_inter_f = np.zeros(n+2)
water_tot_inter_g = np.zeros(n+2)

water_tot_inter_e_heat = np.zeros(n_heat+2)
water_tot_inter_f_heat = np.zeros(n_heat+2)
water_tot_inter_g_heat = np.zeros(n_heat+2)

for i in range(n+1):
    water_tot_inter_e[i] = water_tot_e[i]
    water_tot_inter_f[i] = water_tot_f[i]
    water_tot_inter_g[i] = water_tot_g[i]

for i in range(n_heat+1):
    water_tot_inter_e_heat[i] = water_tot_e_heat[i]
    water_tot_inter_f_heat[i] = water_tot_f_heat[i]
    water_tot_inter_g_heat[i] = water_tot_g_heat[i]

water_tot_inter_e[n+1] = water_tot_1000_e
water_tot_inter_f[n+1] = water_tot_1000_f
water_tot_inter_g[n+1] = water_tot_1000_g

water_tot_inter_e_heat[n_heat+1] = water_tot_1000_e_heat
water_tot_inter_f_heat[n_heat+1] = water_tot_1000_f_heat
water_tot_inter_g_heat[n_heat+1] = water_tot_1000_g_heat

### PLOT ###

fig = plt.figure(num=None, figsize=(10, 9), dpi=300, facecolor='w', edgecolor='k')
fig.suptitle('Water content of the Trappist-1 planets \n at end of magma ocean phase', fontsize=18, fontweight='bold')

plt.plot(M_water_long*factor[0], water_tot_inter_e*factor[0],      color=cmap(0), label='Reference heating')
plt.plot(M_water_long*factor[0], water_tot_inter_e_heat*factor[0], color=cmap(0), label='Extreme heating',    linestyle='--')
plt.plot([factor[2],1000*factor[0]], [factor[2],1000*factor[0]],   color=cmap(0), label='Initial = remaining', linestyle=':')

plt.plot(M_water_long*factor[0], water_tot_inter_e*factor[0], color=cmap(220), label='e')
plt.plot(M_water_long*factor[1], water_tot_inter_f*factor[1], color=cmap(200), label='f')
plt.plot(M_water_long*factor[2], water_tot_inter_g*factor[2], color=cmap(60),  label='g')

plt.plot(M_water_long*factor[0], water_tot_inter_e_heat*factor[0], color=cmap(220), linestyle='--')
plt.plot(M_water_long*factor[1], water_tot_inter_f_heat*factor[1], color=cmap(200), linestyle='--')
plt.plot(M_water_long*factor[2], water_tot_inter_g_heat*factor[2], color=cmap(60),  linestyle='--')

plt.grid(color='grey', which='major', axis='both', linestyle='-')

plt.fill_betweenx([1e-5,1], 100*factor[2], 1000*factor[0], color='whitesmoke', linewidth=0.0)
plt.fill_betweenx([1e-5,1], 100*factor[1], 1000*factor[0], color='lightgrey', linewidth=0.0)
plt.fill_betweenx([1e-5,1], 100*factor[0], 1000*factor[0], color='silver', linewidth=0.0)

plt.text(97*factor[0], 0.6, '$\\mapsto$e', fontsize=18, color='black')
plt.text(97*factor[1], 0.4, '$\\mapsto$f', fontsize=18, color='black')
plt.text(97*factor[2], 0.26, '$\\mapsto$g', fontsize=18, color='black')
plt.text(5e-2, 0.4, 'Extrapolation', fontsize=18, color='black')

plt.legend(loc='best', frameon=True)

plt.xscale('log')
plt.yscale('log')
plt.xlim([factor[2],1000*factor[0]])
plt.ylim([1e-5,1])

plt.xlabel('Initial Water Mass Fraction', fontweight='bold')
plt.ylabel('Remaining Water Mass Fraction', fontweight='bold')

plt.tick_params(axis='both', which='both', direction='in', top=True, right=True)

plt.subplots_adjust(left=0.1, right=0.98, top=0.88, bottom=0.07)
plt.savefig('Final_Water_Trappist1.png')
# plt.savefig('Final_Water_Trappist1.eps', format='eps')
