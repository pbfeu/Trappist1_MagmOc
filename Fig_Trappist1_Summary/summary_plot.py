import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# sns.set_style("whitegrid")
plt.close('all')

cmap=plt.get_cmap('nipy_spectral')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = cmap(0)
mpl.rcParams['axes.labelsize'] = 13
mpl.rcParams['axes.titlesize'] = 14
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 13
mpl.rcParams['axes.titleweight'] = 'bold'


planets = ['e','f','g']
masses  = [0.766,0.926,1.14]
MOLMASSH2O = 18e-3
MOLMASSO2  = 32e-3

color_water = [0,80,220]

Results_TR1_e = np.loadtxt("Results_Trappist1_e.txt", skiprows=2)
Results_TR1_f = np.loadtxt("Results_Trappist1_f.txt", skiprows=2)
Results_TR1_g = np.loadtxt("Results_Trappist1_g.txt", skiprows=2)

M_water = Results_TR1_e[:,0]  # Initial water mass [MO]
n_water = len(M_water)

t_solid_e = Results_TR1_e[:,1]
t_solid_f = Results_TR1_f[:,1]
t_solid_g = Results_TR1_g[:,1]

t_desicc_e = Results_TR1_e[:,2]
t_desicc_f = Results_TR1_f[:,2]
t_desicc_g = Results_TR1_g[:,2]

water_locked_e = Results_TR1_e[:,3]
water_locked_f = Results_TR1_f[:,3]
water_locked_g = Results_TR1_g[:,3]

water_tot_e = Results_TR1_e[:,4]
water_tot_f = Results_TR1_f[:,4]
water_tot_g = Results_TR1_g[:,4]

press_water_e = Results_TR1_e[:,5]
press_water_f = Results_TR1_f[:,5]
press_water_g = Results_TR1_g[:,5]

press_oxy_e = Results_TR1_e[:,6]
press_oxy_f = Results_TR1_f[:,6]
press_oxy_g = Results_TR1_g[:,6]

HZ_entry_e = 253.2
HZ_entry_f = 129.4
HZ_entry_g =  76.3

# find intersection Desiccation & HZ entry
i = 0
while (t_desicc_e[i]<HZ_entry_e):
    last_desicc_e = i
    i = i + 1
i = 0
while (t_desicc_f[i]<HZ_entry_f):
    last_desicc_f = i
    i = i + 1
i = 0
while (t_desicc_g[i]<HZ_entry_g):
    last_desicc_g = i
    i = i + 1
i = 0

M_water_HZ_e = 10**(np.log10(M_water[last_desicc_e]) + (np.log10(HZ_entry_e)-np.log10(t_desicc_e[last_desicc_e])) * (np.log10(M_water[last_desicc_e])-np.log10(M_water[last_desicc_e-1]))/(np.log10(t_desicc_e[last_desicc_e])-np.log10(t_desicc_e[last_desicc_e-1])))
M_water_HZ_f = 10**(np.log10(M_water[last_desicc_f]) + (np.log10(HZ_entry_f)-np.log10(t_desicc_f[last_desicc_f])) * (np.log10(M_water[last_desicc_f])-np.log10(M_water[last_desicc_f-1]))/(np.log10(t_desicc_f[last_desicc_f])-np.log10(t_desicc_f[last_desicc_f-1])))
M_water_HZ_g = 10**(np.log10(M_water[last_desicc_g]) + (np.log10(HZ_entry_g)-np.log10(t_desicc_g[last_desicc_g])) * (np.log10(M_water[last_desicc_g])-np.log10(M_water[last_desicc_g-1]))/(np.log10(t_desicc_g[last_desicc_g])-np.log10(t_desicc_g[last_desicc_g-1])))

M_water_des_e = np.zeros(last_desicc_e+2)
M_water_des_f = np.zeros(last_desicc_f+2)
M_water_des_g = np.zeros(last_desicc_g+2)

t_des_HZ_e = np.zeros(last_desicc_e+2)
t_des_HZ_f = np.zeros(last_desicc_f+2)
t_des_HZ_g = np.zeros(last_desicc_g+2)

for i in range(last_desicc_e+1):
    M_water_des_e[i] = M_water[i]
    t_des_HZ_e[i]    = t_desicc_e[i]
for i in range(last_desicc_f+1):
    M_water_des_f[i] = M_water[i]
    t_des_HZ_f[i]    = t_desicc_f[i]
for i in range(last_desicc_g+1):
    M_water_des_g[i] = M_water[i]
    t_des_HZ_g[i]    = t_desicc_g[i]

M_water_des_e[last_desicc_e+1] = M_water_HZ_e
M_water_des_f[last_desicc_f+1] = M_water_HZ_f
M_water_des_g[last_desicc_g+1] = M_water_HZ_g

t_des_HZ_e[last_desicc_e+1] = HZ_entry_e
t_des_HZ_f[last_desicc_f+1] = HZ_entry_f
t_des_HZ_g[last_desicc_g+1] = HZ_entry_g

Partpress_H2O_e = np.zeros(n_water)
Partpress_O2_e  = np.zeros(n_water)
Partpress_H2O_f = np.zeros(n_water)
Partpress_O2_f  = np.zeros(n_water)
Partpress_H2O_g = np.zeros(n_water)
Partpress_O2_g  = np.zeros(n_water)

for i in range(n_water):
    if (press_water_e[i]==0):
        Partpress_H2O_e[i] = 0
        Partpress_O2_e[i]  = press_oxy_e[i]
    elif (press_oxy_e[i]==0):
        Partpress_H2O_e[i] = press_water_e[i]
        Partpress_O2_e[i]  = 0
    else:
        Partpress_H2O_e[i] = (press_water_e[i] + press_oxy_e[i]) / (1 + ( press_oxy_e[i] * MOLMASSH2O / (press_water_e[i] * MOLMASSO2) ))
        Partpress_O2_e[i]  = (press_water_e[i] + press_oxy_e[i]) / (1 + ( press_water_e[i] * MOLMASSO2 / (press_oxy_e[i] * MOLMASSH2O) ))

    if (press_water_f[i]==0):
        Partpress_H2O_f[i] = 0
        Partpress_O2_f[i]  = press_oxy_f[i]
    elif (press_oxy_f[i]==0):
        Partpress_H2O_f[i] = press_water_f[i]
        Partpress_O2_f[i]  = 0
    else:
        Partpress_H2O_f[i] = (press_water_f[i] + press_oxy_f[i]) / (1 + ( press_oxy_f[i] * MOLMASSH2O / (press_water_f[i] * MOLMASSO2) ))
        Partpress_O2_f[i]  = (press_water_f[i] + press_oxy_f[i]) / (1 + ( press_water_f[i] * MOLMASSO2 / (press_oxy_f[i] * MOLMASSH2O) ))

    if (press_water_g[i]==0):
        Partpress_H2O_g[i] = 0
        Partpress_O2_g[i]  = press_oxy_g[i]
    elif (press_oxy_g[i]==0):
        Partpress_H2O_g[i] = press_water_g[i]
        Partpress_O2_g[i]  = 0
    else:
        Partpress_H2O_g[i] = (press_water_g[i] + press_oxy_g[i]) / (1 + ( press_oxy_g[i] * MOLMASSH2O / (press_water_g[i] * MOLMASSO2) ))
        Partpress_O2_g[i]  = (press_water_g[i] + press_oxy_g[i]) / (1 + ( press_water_g[i] * MOLMASSO2 / (press_oxy_g[i] * MOLMASSH2O) ))

### PLOT ###

fig = plt.figure(num=None, figsize=(9, 8), dpi=300, facecolor='w', edgecolor='k')

# ----------------------------------------------------------------------------------------------------------------- #
ax1 = fig.add_subplot(221)

ax1.plot(M_water, t_solid_e,          color=cmap(0), label='M.O. Solidification')
ax1.plot(M_water_des_e, t_des_HZ_e,   color=cmap(0), label='Atm. desiccation',  linestyle='--')
ax1.scatter(M_water_HZ_e, HZ_entry_e, color=cmap(0), label='Atm. escape stopps', marker='o')

ax1.plot(M_water, t_solid_e, color=cmap(220))
ax1.plot(M_water, t_solid_f, color=cmap(200))
ax1.plot(M_water, t_solid_g, color=cmap(60))

ax1.plot(M_water_des_e, t_des_HZ_e, color=cmap(220), linestyle='--')
ax1.plot(M_water_des_f, t_des_HZ_f, color=cmap(200), linestyle='--')
ax1.plot(M_water_des_g, t_des_HZ_g, color=cmap(60),  linestyle='--')

ax1.scatter(M_water_HZ_e, HZ_entry_e, color=cmap(220), marker='o')
ax1.scatter(M_water_HZ_f, HZ_entry_f, color=cmap(200), marker='o')
ax1.scatter(M_water_HZ_g, HZ_entry_g, color=cmap(60),  marker='o')

ax1.legend(loc='best', frameon=True)

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.set_ylim([1,300])

ax1.set_ylabel('Time (Myr)', fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #
ax2 = fig.add_subplot(222)

ax2.plot(M_water, water_tot_e,    color=cmap(0), label='Total')
ax2.plot(M_water, water_locked_e, color=cmap(0), label='Solid', linestyle='--')

ax2.plot(M_water, water_tot_e,     color=cmap(220))
ax2.plot(M_water, water_tot_f,     color=cmap(200))
ax2.plot(M_water, water_tot_g,     color=cmap(60))

ax2.plot(M_water, water_locked_e,     color=cmap(220), linestyle='--')
ax2.plot(M_water, water_locked_f,     color=cmap(200), linestyle='--')
ax2.plot(M_water, water_locked_g,     color=cmap(60),  linestyle='--')

ax2.plot(M_water, M_water, color='lightgrey', label='Initial')

ax2.legend(loc='best', frameon=True)

ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.set_ylabel('Water Remaining (TO)', fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #
ax3 = fig.add_subplot(223)

ax3.plot(M_water, Partpress_H2O_e,     label='e',          color=cmap(220))
ax3.plot(M_water, Partpress_H2O_f,     label='f',          color=cmap(200))
ax3.plot(M_water, Partpress_H2O_g,     label='g',          color=cmap(60))

ax3.legend(loc='lower left', bbox_to_anchor= (0, 2.15), ncol=4, borderaxespad=0, frameon=True)

ax3.set_xscale('log')
ax3.set_yscale('log')

ax3.set_ylim([1e2,3e4])

ax3.set_xlabel('Initial Water Mass (TO)', fontweight='bold')
ax3.set_ylabel('Partial Water Pressure (bar)', fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #
ax4 = fig.add_subplot(224)

ax4.plot(M_water, Partpress_O2_e,     color=cmap(220))
ax4.plot(M_water, Partpress_O2_f,     color=cmap(200))
ax4.plot(M_water, Partpress_O2_g,     color=cmap(60))

ax4.set_ylim([80,1e3])

ax4.set_xscale('log')
ax4.set_yscale('log')

ax4.set_xlabel('Initial Water Mass (TO)', fontweight='bold')
ax4.set_ylabel('Partial Oxygen Pressure (bar)', fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #

plt.subplots_adjust(left=0.08, right=0.98, top=0.93, bottom=0.07, wspace=0.23, hspace=0.1)
plt.savefig('Summary_Trappist1.eps', format='eps')
# plt.savefig('Summary_Trappist1.png', format='png')
