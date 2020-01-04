import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.close('all')

cmap=plt.get_cmap('nipy_spectral')
mpl.rcParams['lines.linewidth']  = 2
mpl.rcParams['lines.color']      = cmap(0)
mpl.rcParams['axes.labelsize']   = 13
mpl.rcParams['axes.titlesize']   = 14
mpl.rcParams['xtick.labelsize']  = 12
mpl.rcParams['ytick.labelsize']  = 12
mpl.rcParams['legend.fontsize']  = 12
mpl.rcParams['axes.titleweight'] = 'bold'


planets = ['e','f','g']
masses  = [0.766,0.926,1.14]

color_water = [0,80,220]

Results_TR1_g = np.loadtxt("Results_Trappist1_g.txt", skiprows=2)

M_water = Results_TR1_g[:,0]  # Initial water mass [MO]

t_solid_g  = Results_TR1_g[:,1]
t_desicc_g = Results_TR1_g[:,2]

HZ_entry_g =  76.3

# find intersection Desiccation & HZ entry
i = 0
while (t_desicc_g[i]<HZ_entry_g):
    last_desicc_g = i
    i = i + 1

M_water_HZ_g  = 10**(np.log10(M_water[last_desicc_g]) + (np.log10(HZ_entry_g)-np.log10(t_desicc_g[last_desicc_g])) * (np.log10(M_water[last_desicc_g])-np.log10(M_water[last_desicc_g-1]))/(np.log10(t_desicc_g[last_desicc_g])-np.log10(t_desicc_g[last_desicc_g-1])))
M_water_des_g = np.zeros(last_desicc_g+2)

t_des_HZ_g = np.zeros(last_desicc_g+2)

for i in range(last_desicc_g+1):
    M_water_des_g[i] = M_water[i]
    t_des_HZ_g[i]    = t_desicc_g[i]

M_water_des_g[last_desicc_g+1] = M_water_HZ_g
t_des_HZ_g[last_desicc_g+1]    = HZ_entry_g

t_des_HZ_g_tot    = np.append(t_des_HZ_g,HZ_entry_g)
M_water_des_g_tot = np.append(M_water_des_g,100)

### PLOT ###

fig = plt.figure(num=None, figsize=(5, 4.9), dpi=300, facecolor='w', edgecolor='k')

# ----------------------------------------------------------------------------------------------------------------- #
ax1 = fig.add_subplot(111)

ax1.plot(M_water,       t_solid_g,  color=cmap(0), label='Solidification')
ax1.plot(M_water_des_g, t_des_HZ_g, color=cmap(0), label='Atm. desiccation', linestyle='--')

ax1.fill_between(M_water_des_g,      t_des_HZ_g, 300,            color='red',    alpha=0.3, linewidth=0.0)
ax1.fill_between([M_water_HZ_g,100], HZ_entry_g, 300,            color='blue',   alpha=0.3, linewidth=0.0)
ax1.fill_between(M_water_des_g_tot,  1,          t_des_HZ_g_tot, color='yellow', alpha=0.3, linewidth=0.0)

ax1.axvline(x=2, ymax=0.8, linewidth=4, color='magenta', linestyle=':')
ax1.axvline(x=5, ymax=0.8, linewidth=4, color='magenta', linestyle=':')
ax1.axvline(x=100,         linewidth=4, color='magenta', linestyle=':')

ax1.text(  2, 1, 'Scenario 1', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')
ax1.text(  5, 1, 'Scenario 2', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')
ax1.text(100, 1, 'Scenario 3', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')

ax1.text(1.1, 120, 'Atmosphere \ndesiccated',        color='red',    fontsize=16)
ax1.text(  8, 120, 'Water survives \nin atmosphere', color='blue',   fontsize=16)
ax1.text(  8,  25, 'Ongoing \nwater loss',           color='orange', fontsize=16)

ax1.legend(title='TRAPPIST-1 g with $H_2O$ atmosphere', loc='lower left', bbox_to_anchor= (0, 1.02), ncol=2, borderaxespad=0, frameon=True, title_fontsize=13)

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.set_xlim([1,105])
ax1.set_ylim([1,300])

ax1.set_xlabel('Initial Water Mass (TO)', fontweight='bold')
ax1.set_ylabel('Time (Myr)',              fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #
plt.subplots_adjust(left=0.15, right=0.97, top=0.83, bottom=0.12, wspace=0.23, hspace=0.23)
plt.savefig('Summary_Trappist1_scenarios_g.png')
