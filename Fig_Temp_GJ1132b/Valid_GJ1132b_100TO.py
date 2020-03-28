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
mpl.rcParams['axes.labelsize'] = 13
mpl.rcParams['axes.labelweight'] = 'bold'
mpl.rcParams['xtick.labelsize'] = 12
mpl.rcParams['ytick.labelsize'] = 12
mpl.rcParams['legend.fontsize'] = 12
######################
cmap=plt.get_cmap('nipy_spectral')

#------------------------------------------------------------------------------#
# Temperature evolution

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



#------------------------------------------------------------------------------#
# Oxygen Pressure
WaterFracIni  = [0.0014,0.014,0.14,1.4] # in weight percent, corresponds to 0.1,1,10,100 terrestrial oceans

# Results for GJ1132b with VPLanet
Water_grey = [0.1, 85, 90, 95, 100] # in Myr, no escape
Oxy_grey   = [  0,  0, 30, 68, 107] # in Myr, XUV-abs eff. = 0.15

Water_petit = [0.1, 130, 135, 140, 150,  200] # in Myr, XUV-abs eff. = 0.3
Oxy_petit   = [  0,   0,  12,  71, 241, 2844]

# Results from Schaefer et al. (2016), Figure 7a
SchaeferWater = [ 100,222,254,306,341,806,985,1131,1249,1356]
SchaeferOxy   = [0,1e-5,1e-4,1e-3,1e-2,1e-1,1e0,1e1,1e2,1e3]

#------------------------------------------------------------------------------#
# Solidification time
WaterMassIni  = [0.1,1,10,100] # in weight percent, corresponds to 0.1,1,10,100 terrestrial oceans
WaterMassIni_petit  = [0.1,1,10,100,150,200]
# Results for GJ1132b with VPLanet
New_grey  = [0.0196, 0.201, 2.29, 63.9]
New_petit = [0.0202, 0.206, 2.34, 65.2, 165,550]

# Results from Schaefer et al. (2016), Figure 5
SchaeferWaterTO = [ (10**-2.7)/0.014,(10**-1.7)/0.014,  (10**-1)/0.014, (10**-0.7)/0.014,(10**-0.01)/0.014,(10**0.69)/0.014,  (10**1)/0.014,(10**1.27)/0.014]
SchaeferA     = [10**-2.26,10**-1.3,10**-0.6,10**-0.28,10**0.823, 10**2.6,10**3.1, 10**3.7]

#------------------------------------------------------------------------------#
### PLOT ###
fig = plt.figure(num=None, figsize=(9, 6.8), dpi=300, facecolor='w', edgecolor='k')
gs = fig.add_gridspec(5, 2)
ax1 = fig.add_subplot(gs[0:2,:])
ax2 = fig.add_subplot(gs[2:, 1])
ax3 = fig.add_subplot(gs[2:, 0])
#------------------------------------------------------------------------------#
# ax1 = plt.subplot(221)
ax1.plot(Time_schaefer,   T_p_schaefer, label='Schaefer et al., 2016',    color=cmap(50) )
ax1.plot(time*1e-6,       Tpot,         label='VPLanet: grey atmosphere', color=cmap(200))
ax1.plot(time_petit*1e-6, Tpot_petit,   label='VPLanet: $petitCODE$',       color=cmap(220))

# Dashed lines indicate solidification time for different scenarios
ax1.axvline(x=time_petit[len(time)-1]*1e-6,           ymax=0.5, color=cmap(220), linestyle='--')
ax1.axvline(x=time[len(time)-1]*1e-6,       ymin=0.5, ymax=1,   color=cmap(200), linestyle='--')
ax1.axvline(x=10**1.555,                                        color=cmap(50),  linestyle='--')

ax1.text(100, 4050, 'Solidification', ha='right', fontsize=16)
ax1.legend(loc='lower left', bbox_to_anchor= (-0.09, 1.1), ncol=3, frameon=True, fontsize=13)

# ax1.legend(loc='best', frameon=True, fontsize=12)

ax1.set_xlim([1e-4,1e2])
ax1.set_ylim([1500,4000])

ax1.set_xscale('log')
ax1.set_ylabel('Temperature (K)')
ax1.set_xlabel('Time (Myr)')

#------------------------------------------------------------------------------#
ax2.plot(Water_grey, Oxy_grey, label='VPLanet (grey)', color=cmap(200), linewidth=3.0)
ax2.plot(Water_petit, Oxy_petit, label='VPLanet (petit)', color=cmap(220), linewidth=3.0)
ax2.plot(SchaeferWater, SchaeferOxy, label='Schaefer (XUV-Model A)', color='b', linewidth=3.0)
ax2.axvline(x=100,         linewidth=4, color='magenta', linestyle=':')
ax2.text(90,6e2,'Scenario in top panel',color='magenta',fontsize=14,ha='right')
# ax2.legend(loc='best', frameon=True, fontsize=14)
ax2.set_xlabel('Initial Water Mass (TO)')
ax2.set_ylabel('Final oxygen pressure (bar)')
ax2.set_xlim([8e-2,2e3])
# ax2.set_ylim([1e-5,1e4])
ax2.set_xscale('log')
ax2.set_yscale('symlog', linthreshy=1e-4)
#------------------------------------------------------------------------------#
ax3.plot(SchaeferWaterTO, SchaeferA, label='Schaefer et al. (2016)', color='b', linewidth=3.0)
ax3.plot(WaterMassIni, New_grey, label='VPLanet: grey atmosphere', color=cmap(200), linewidth=3.0)

ax3.plot(WaterMassIni_petit, New_petit, label='VPLanet: petitCODE', color=cmap(220), linewidth=3.0)#, linestyle=':')
ax3.plot(WaterMassIni, New_grey, color=cmap(200), linewidth=3.0, linestyle='--')
ax3.axvline(x=100,         linewidth=4, color='magenta', linestyle=':')
ax3.text(90,1e3,'Scenario in top panel',color='magenta',fontsize=14,ha='right')

# ax3.legend(frameon=True, fontsize=14, loc='lower right', bbox_to_anchor= (1, 1.02e4), ncol=3)
ax3.set_xlabel('Initial Water Mass (TO)')
ax3.set_ylabel('Solidification Time (Myr)')
ax3.set_xlim([8e-2,2e3])
ax3.set_ylim([4e-3,6e3])
ax3.set_xscale('log')
ax3.set_yscale('log')
#------------------------------------------------------------------------------#
plt.subplots_adjust(left=0.1, right=0.97, top=0.9, bottom=0.1, wspace=0.3, hspace=0.9)
# plt.savefig('Valid_GJ1132b_100TO_Schaefer_Grey_Petit.png')
plt.savefig('Valid_GJ1132b_100TO_Schaefer_Grey_Petit.eps', format='eps')
