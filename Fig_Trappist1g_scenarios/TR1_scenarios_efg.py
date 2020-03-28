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

Results_TR1_e = np.loadtxt("Results_Trappist1_e.txt", skiprows=2)
Results_TR1_f = np.loadtxt("Results_Trappist1_f.txt", skiprows=2)
Results_TR1_g = np.loadtxt("Results_Trappist1_g.txt", skiprows=2)

M_water = Results_TR1_g[:,0]  # Initial water mass [MO]

t_solid_g  = Results_TR1_g[:,1]
t_desicc_g = Results_TR1_g[:,2]
t_solid_e = Results_TR1_e[:,1]
t_solid_f = Results_TR1_f[:,1]
t_desicc_e = Results_TR1_e[:,2]
t_desicc_f = Results_TR1_f[:,2]

HZ_entry_g =  76.3
HZ_entry_e = 253.2
HZ_entry_f = 129.4

# find intersection Desiccation & HZ entry
i = 0
while (t_desicc_g[i]<HZ_entry_g):
    last_desicc_g = i
    i = i + 1
i = 0
while (t_desicc_e[i]<HZ_entry_e):
    last_desicc_e = i
    i = i + 1
i = 0
while (t_desicc_f[i]<HZ_entry_f):
    last_desicc_f = i
    i = i + 1

M_water_HZ_g  = 10**(np.log10(M_water[last_desicc_g]) + (np.log10(HZ_entry_g)-np.log10(t_desicc_g[last_desicc_g])) * (np.log10(M_water[last_desicc_g])-np.log10(M_water[last_desicc_g-1]))/(np.log10(t_desicc_g[last_desicc_g])-np.log10(t_desicc_g[last_desicc_g-1])))
M_water_des_g = np.zeros(last_desicc_g+2)

M_water_HZ_e = 10**(np.log10(M_water[last_desicc_e]) + (np.log10(HZ_entry_e)-np.log10(t_desicc_e[last_desicc_e])) * (np.log10(M_water[last_desicc_e])-np.log10(M_water[last_desicc_e-1]))/(np.log10(t_desicc_e[last_desicc_e])-np.log10(t_desicc_e[last_desicc_e-1])))
M_water_HZ_f = 10**(np.log10(M_water[last_desicc_f]) + (np.log10(HZ_entry_f)-np.log10(t_desicc_f[last_desicc_f])) * (np.log10(M_water[last_desicc_f])-np.log10(M_water[last_desicc_f-1]))/(np.log10(t_desicc_f[last_desicc_f])-np.log10(t_desicc_f[last_desicc_f-1])))
M_water_des_e = np.zeros(last_desicc_e+2)
M_water_des_f = np.zeros(last_desicc_f+2)

t_des_HZ_g = np.zeros(last_desicc_g+2)
t_des_HZ_e = np.zeros(last_desicc_e+2)
t_des_HZ_f = np.zeros(last_desicc_f+2)

for i in range(last_desicc_g+1):
    M_water_des_g[i] = M_water[i]
    t_des_HZ_g[i]    = t_desicc_g[i]
for i in range(last_desicc_e+1):
    M_water_des_e[i] = M_water[i]
    t_des_HZ_e[i]    = t_desicc_e[i]
for i in range(last_desicc_f+1):
    M_water_des_f[i] = M_water[i]
    t_des_HZ_f[i]    = t_desicc_f[i]

M_water_des_g[last_desicc_g+1] = M_water_HZ_g
t_des_HZ_g[last_desicc_g+1]    = HZ_entry_g
M_water_des_e[last_desicc_e+1] = M_water_HZ_e
M_water_des_f[last_desicc_f+1] = M_water_HZ_f
t_des_HZ_e[last_desicc_e+1] = HZ_entry_e
t_des_HZ_f[last_desicc_f+1] = HZ_entry_f

t_des_HZ_g_tot    = np.append(t_des_HZ_g,HZ_entry_g)
M_water_des_g_tot = np.append(M_water_des_g,100)

t_des_HZ_e_tot    = np.append(t_des_HZ_e,HZ_entry_e)
M_water_des_e_tot = np.append(M_water_des_e,100)
t_des_HZ_f_tot    = np.append(t_des_HZ_f,HZ_entry_f)
M_water_des_f_tot = np.append(M_water_des_f,100)

### PLOT ###

fig = plt.figure(num=None, figsize=(9, 4.3), dpi=1200, facecolor='w', edgecolor='k')

# ----------------------------------------------------------------------------------------------------------------- #
ax1 = fig.add_subplot(121)

ax1.plot(M_water,       t_solid_g,  color=cmap(60), label='Solidification')
# ax1.plot(M_water_des_g, t_des_HZ_g, color=cmap(60), label='Atm. desiccation', linestyle='--')

ax1.fill_between(M_water_des_g,      t_des_HZ_g, 300,            color='red',    alpha=0.3, linewidth=0.0)
ax1.fill_between([M_water_HZ_g,100], HZ_entry_g, 300,            color='blue',   alpha=0.3, linewidth=0.0)
ax1.fill_between(M_water_des_g_tot,  1,          t_des_HZ_g_tot, color='yellow', alpha=0.3, linewidth=0.0)

ax1.axvline(x=2, ymax=0.8, linewidth=4, color='magenta', linestyle=':')
ax1.axvline(x=5, ymax=0.8, linewidth=4, color='magenta', linestyle=':')
ax1.axvline(x=100,         linewidth=4, color='magenta', linestyle=':')

ax1.text(  2, 1, 'Ex. Scenario 1', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')
ax1.text(  5, 1, 'Ex. Scenario 2', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')
ax1.text(100, 1, 'Ex. Scenario 3', rotation=90, ha='right', va='bottom', fontsize=14, color='magenta')

ax1.text(1.1, 120, 'Atmosphere \ndesiccated',        color='black',    fontsize=16)
ax1.text(  8, 120, 'Water survives \nin atmosphere', color='black',   fontsize=16)
ax1.text(  8,  25, 'Ongoing \nwater loss',           color='black', fontsize=16)

# ax1.legend(title='TRAPPIST-1 g with $H_2O$ atmosphere', loc='lower left', bbox_to_anchor= (0, 1.02), ncol=2, borderaxespad=0, frameon=True, title_fontsize=13)

ax1.set_xscale('log')
ax1.set_yscale('log')

ax1.set_xlim([1,105])
ax1.set_ylim([1,300])

ax1.set_xlabel('Initial Water Mass (TO)',   fontweight='bold')
ax1.set_ylabel('Solidification Time (Myr)', fontweight='bold')

# ----------------------------------------------------------------------------------------------------------------- #
ax2 = fig.add_subplot(122)

# ax2.plot(M_water, t_solid_e, color=cmap(0), label='Solidification')
# ax2.plot(M_water_des_e, t_des_HZ_e, color=cmap(0), linestyle='--', label='Atm. desiccation')
# ax2.scatter(M_water_HZ_e, HZ_entry_e, color=cmap(0), marker='o', label='HZ entry')

ax2.plot(M_water, t_solid_e, color=cmap(220), label='e')
ax2.plot(M_water, t_solid_f, color=cmap(200), label='f')
ax2.plot(M_water, t_solid_g, color=cmap(60) , label='g')

# ax2.plot(M_water_des_e, t_des_HZ_e, color=cmap(220), linestyle='--')
# ax2.plot(M_water_des_f, t_des_HZ_f, color=cmap(200), linestyle='--')
# ax2.plot(M_water_des_g, t_des_HZ_g, color=cmap(60),  linestyle='--')

ax2.fill_between([7,9], 3, 200, color='grey',   alpha=0.3, linewidth=0.0)
ax2.fill_between([6,8,10.5], [3,2,3], [3,3,3], color='grey',   alpha=0.3, linewidth=0.0)
ax2.text(9,1.8,'Distance from star',color='grey',fontsize=14,ha='center',va='top')

ax2.fill_between([1,8], 70, 110, color=cmap(220),   alpha=0.3, linewidth=0.0)
ax2.text(1.5,80,'Scenario 1',color=cmap(0),fontsize=14)
ax2.fill_between([9,105], 70, 110, color=cmap(220),   alpha=0.3, linewidth=0.0)
ax2.text(15,80,'Scenario 2',color=cmap(0),fontsize=14)

ax2.fill_between([1,4], 30, 47, color=cmap(200),   alpha=0.3, linewidth=0.0)
ax2.text(2,34,'1',color=cmap(0),fontsize=14)
ax2.fill_between([4.5,105], 30, 47, color=cmap(200),   alpha=0.3, linewidth=0.0)
ax2.text(20,34,'2',color=cmap(0),fontsize=14)

ax2.fill_between([1,2.3], 7, 11, color=cmap(60),   alpha=0.3, linewidth=0.0)
ax2.text(1.1,8,'1',color=cmap(0),fontsize=14)
ax2.fill_between([2.5,50], 7, 11, color=cmap(60),   alpha=0.3, linewidth=0.0)
ax2.text(10,8,'2',color=cmap(0),fontsize=14)
ax2.fill_between([55,105], 7, 11, color=cmap(60),   alpha=0.3, linewidth=0.0)
ax2.text(70,8,'3',color=cmap(0),fontsize=14)

# ax2.legend(loc='lower left', bbox_to_anchor= (-0.6, 1.02), ncol=3, borderaxespad=0, frameon=True)
ax2.legend(loc='upper left', ncol=3, frameon=True)

# ax2.scatter(M_water_HZ_e, HZ_entry_e, color=cmap(220), marker='o')#, linestyle='None')
# ax2.scatter(M_water_HZ_f, HZ_entry_f, color=cmap(200), marker='o')#, linestyle='None')
# ax2.scatter(M_water_HZ_g, HZ_entry_g, color=cmap(60),  marker='o')#, linestyle='None')

# ax2.legend(loc='best', frameon=True)

ax2.set_xscale('log')
ax2.set_yscale('log')

ax2.set_xlim([1,105])
ax2.set_ylim([1,300])

ax2.set_xlabel('Initial Water Mass (TO)', fontweight='bold')
# ax2.set_ylabel('Time (Myr)', fontweight='bold')
# ----------------------------------------------------------------------------------------------------------------- #

plt.subplots_adjust(left=0.1, right=0.97, top=0.95, bottom=0.12, wspace=0.23, hspace=0.23)
# plt.savefig('Summary_Trappist1_scenarios_efg.png')
plt.savefig('Summary_Trappist1_scenarios_efg.pdf', format='pdf')
