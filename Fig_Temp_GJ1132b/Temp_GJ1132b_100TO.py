import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#####################################
# Plot results from VPLanet/MagmOc  #
#   For GJ1132b with 100TO water    #
# for grey atmosphere and petitCODE #
#      And Comapare to results      #
#     from Schaefer et al. 2016     #
#####################################

plt.close('all')

# Set style for plot #
mpl.rcParams['lines.linewidth'] = 3
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['axes.labelweight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 13
mpl.rcParams['ytick.labelsize'] = 13
mpl.rcParams['legend.fontsize'] = 12
######################
cmap=plt.get_cmap('nipy_spectral')

# import data from VPLanet runs
data_grey  = np.loadtxt("GJ_eps03_100TO_grey/GJ1132.GJ1132b.forward")
data_petit = np.loadtxt("GJ_eps03_100TO_petit/GJ1132.GJ1132b.forward")

time        = data_grey[:,0]   # time (yr)
Tpot        = data_grey[:,1]   # Potential temp magma ocean (K)

time_petit  = data_petit[:,0]  # time (yr)
Tpot_petit  = data_petit[:,1]  # Potential temp magma ocean (K)

# data from Schaefer et al. 2016, Figure 4: blue, solid line
Time_schaefer   = [  -6,   -4, -3.7, -3.4,   -3,   -2, -1.5, -1.15, -0.9,    0,  0.6,  0.8,  1.2, 1.35, 1.53, 1.555, 1.57,    2]
for i in range(len(Time_schaefer)):
    Time_schaefer[i] = 10**(Time_schaefer[i])
T_p_schaefer    = [4000, 3980, 3940, 3869, 3680, 3100, 2845,  2725, 2675, 2625, 2585, 2550, 2355, 2260, 2100,  1640, 1638, 1570]

# plot
fig = plt.figure(num=None, figsize=(6, 3), dpi=300, facecolor='w', edgecolor='k')

plt.plot(Time_schaefer,   T_p_schaefer, label='Schaefer et al., 2016',    color=cmap(50) )
plt.plot(time*1e-6,       Tpot,         label='VPLanet: grey atmosphere', color=cmap(200))
plt.plot(time_petit*1e-6, Tpot_petit,   label='VPLanet: petitCODE',       color=cmap(220))

# Dashed lines indicate solidification time for different scenarios
plt.axvline(x=time_petit[len(time)-1]*1e-6,           ymax=0.5, color=cmap(220), linestyle='--')
plt.axvline(x=time[len(time)-1]*1e-6,       ymin=0.5, ymax=1,   color=cmap(200), linestyle='--')
plt.axvline(x=10**1.555,                                        color=cmap(50),  linestyle='--')

plt.text(100, 4050, 'Solidification', ha='right', fontsize=16)

plt.legend(loc='best', frameon=True, fontsize=12)

plt.xlim([1e-6,1e2])
plt.ylim([1500,4000])

plt.xscale('log')
plt.ylabel('Temperature (K)')
plt.xlabel('Time (Myr)')

plt.tight_layout()

plt.savefig('Temp_GJ1132b_100TO_Schaefer_Grey_Petit.png')
