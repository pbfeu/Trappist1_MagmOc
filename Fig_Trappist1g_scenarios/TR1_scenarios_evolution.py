import numpy as np
import matplotlib as mpl
import matplotlib.pyplot  as plt
import seaborn as sns
from collections import OrderedDict

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

# read data
TR1_g_1   = np.loadtxt("TR1_g_1TO/Trappist1.g.forward")
TR1_g_5   = np.loadtxt("TR1_g_5TO/Trappist1.g.forward")
TR1_g_100 = np.loadtxt("TR1_g_100TO/Trappist1.g.forward")

time_1        = TR1_g_1[:,0]  # time (yr)
Tpot_1        = TR1_g_1[:,1]  # Potential temp magma ocean (K)
Tsurf_1       = TR1_g_1[:,2]  # Surface temp (K)
Press_H2O_1   = TR1_g_1[:,8]  # pressure water in atmopshere (bar)
Press_O_1     = TR1_g_1[:,9]  # pressure oxygen in atmosphere (bar)

time_5        = TR1_g_5[:,0]  # time (yr)
Tpot_5        = TR1_g_5[:,1]  # Potential temp magma ocean (K)
Tsurf_5       = TR1_g_5[:,2]  # Surface temp (K)
Press_H2O_5   = TR1_g_5[:,8]  # pressure water in atmopshere (bar)
Press_O_5     = TR1_g_5[:,9]  # pressure oxygen in atmosphere (bar)

time_100        = TR1_g_100[:,0]  # time (yr)
Tpot_100        = TR1_g_100[:,1]  # Potential temp magma ocean (K)
Tsurf_100       = TR1_g_100[:,2]  # Surface temp (K)
Press_H2O_100   = TR1_g_100[:,8]  # pressure water in atmopshere (bar)
Press_O_100     = TR1_g_100[:,9]  # pressure oxygen in atmosphere (bar)

n_time_1   = len(time_1)
n_time_5   = len(time_5)
n_time_100 = len(time_100)
t_start    = time_1[1]*1e-6
t_end2     = time_1[n_time_1-1]*1e-6
t_end5     = time_5[n_time_5-1]*1e-6
t_end100   = time_100[n_time_100-1]*1e-6

### Plot ###
fig = plt.figure(num=None, figsize=(12, 12), dpi=300, facecolor='w', edgecolor='k')

# ---------------------------------------------------------------------------- #
ax1 = fig.add_subplot(321)

ax1.axvspan( t_start, t_end2, color='yellow', alpha=0.3, linewidth=0.0)
ax1.axvspan(  t_end2,    200, color='red',    alpha=0.3, linewidth=0.0)

ax1.plot(time_1*10**-6, Tpot_1,  label='$T_\\mathrm{p}$',      color=cmap(0))
# ax1.plot(time_1*10**-6, Tsurf_1, label='$T_{surf}$', color=cmap(110))

ax1.text(2e-3, 4100, 'Scenario 1: 1TO', fontsize=16, color='magenta')

ax1.text(1e-2, 3000, 'I', fontsize=16, color='magenta')
ax1.text(   1, 2100, 'II,III', fontsize=16, color='magenta')
# ax1.text(   5, 1900, 'III', fontsize=16, color='magenta')
ax1.text(  20, 600, 'IV & V', fontsize=16, color='magenta')


ax1.legend(loc='lower left', bbox_to_anchor= (0, 1.05), ncol=2, borderaxespad=0, frameon=True)

ax1.set_ylabel('Temperature (K)')
ax1.set_xscale('log')
ax1.set_xlim([t_start,200])
ax1.set_ylim([500,4500])

# ---------------------------------------------------------------------------- #
ax2 = fig.add_subplot(322, sharex=ax1)

ax2.axvspan( t_start, t_end2, color='yellow', alpha=0.3, linewidth=0.0)
ax2.axvspan(  t_end2,    200, color='red',    alpha=0.3, linewidth=0.0)

ax2.plot(time_1*10**-6, Press_H2O_1, label='$\\rm{H_2O}$', color='blue')
ax2.plot(time_1*10**-6, Press_O_1,   label='$\\rm{O_2}$',  color='red')

ax2.text(2e-3, 1e4, 'Scenario 1: 1TO', fontsize=16, color='magenta')

ax2.text(1e-2, 1e2, 'I', fontsize=16, color='magenta')
ax2.text(   1, 5e2, 'II,III', fontsize=16, color='magenta')
# ax2.text(   5, 2e2, 'III', fontsize=16, color='magenta')
ax2.text(  20,   10, 'IV & V', fontsize=16, color='magenta')

ax2.legend(loc='lower left', bbox_to_anchor= (0, 1.05), ncol=2, borderaxespad=0, frameon=True)

ax2.set_yscale('log')
ax2.set_ylim([1,3e4])

ax2.set_ylabel('Atmospheric pressure (bar)')

# ---------------------------------------------------------------------------- #
ax3 = fig.add_subplot(323, sharex=ax1)

ax3.axvspan(t_start, t_end5, color='yellow', alpha=0.3, linewidth=0.0)
ax3.axvspan( t_end5,    200, color='red',    alpha=0.3, linewidth=0.0)

ax3.plot(time_5*10**-6, Tpot_5,  label='$T_p$',    color=cmap(0))
# ax3.plot(time_5*10**-6, Tsurf_5, label='$T_surf$', color=cmap(110))

ax3.text(2e-3, 4100, 'Scenario 2: 5TO', fontsize=16, color='magenta')

ax3.text(5e-2, 3000, 'I', fontsize=16, color='magenta')
ax3.text(   1, 2100, 'II,III', fontsize=16, color='magenta')
# ax3.text(   5, 1900, 'III', fontsize=16, color='magenta')
ax3.text(  45, 2300, 'V', fontsize=16, color='magenta')
ax3.text( 100,  600, 'IV', fontsize=16, color='magenta')

ax3.set_ylabel('Temperature (K)')
ax3.set_ylim([500,4500])

# ---------------------------------------------------------------------------- #
ax4 = fig.add_subplot(324, sharex=ax1)

ax4.axvspan(t_start, t_end5, color='yellow', alpha=0.3, linewidth=0.0)
ax4.axvspan( t_end5,    200, color='red',    alpha=0.3, linewidth=0.0)

ax4.plot(time_5*10**-6, Press_H2O_5, label='$H_2O$', color='blue')
ax4.plot(time_5*10**-6, Press_O_5,   label='$O_2$',  color='red')

ax4.text(2e-3, 1e4, 'Scenario 2: 5TO', fontsize=16, color='magenta')

ax4.text(5e-2, 6e2,  'I', fontsize=16, color='magenta')
ax4.text(   1, 2e3, 'II,III', fontsize=16, color='magenta')
ax4.text(  45, 2e3,  'V', fontsize=16, color='magenta')
ax4.text( 100,   4, 'IV', fontsize=16, color='magenta')

ax4.set_yscale('log')
ax4.set_ylim([1,3e4])

ax4.set_ylabel('Atmospheric pressure (bar)')

# ---------------------------------------------------------------------------- #
ax5 = fig.add_subplot(325, sharex=ax1)

ax5.axvspan( t_start, t_end100, color='yellow',  alpha=0.3, linewidth=0.0)
ax5.axvspan(t_end100,      200, color='blue',    alpha=0.3, linewidth=0.0)

ax5.plot(time_100*10**-6, Tpot_100,  label='$T_p$',      color=cmap(0))
# ax5.plot(time_100*10**-6, Tsurf_100, label='$T_{surf}$', color=cmap(110))

ax5.text(2e-3, 4100, 'Scenario 3: 100TO', fontsize=16, color='magenta')

ax5.text(  3, 3000, 'I', fontsize=16, color='magenta')
ax5.text( 25, 2100, 'IV', fontsize=16, color='magenta')
ax5.text(  2, 1000, 'V', fontsize=16, color='magenta')
ax5.text(100,  600, 'VI', fontsize=16, color='magenta')

ax5.set_xlabel('Time (Myr)')
ax5.set_ylabel('Temperature (K)')
ax5.set_ylim([500,4500])

# ---------------------------------------------------------------------------- #
ax6 = fig.add_subplot(326, sharex=ax1)

ax6.axvspan( t_start, t_end100, color='yellow', alpha=0.3, linewidth=0.0)
ax6.axvspan(t_end100,      200, color='blue',   alpha=0.3, linewidth=0.0)

ax6.plot(time_100*10**-6, Press_H2O_100, label='$H_2O$', color='blue')
ax6.plot(time_100*10**-6, Press_O_100,   label='$O_2$',  color='red')

ax6.text(2e-3, 1e4, 'Scenario 3: 100TO', fontsize=16, color='magenta')

ax6.text(  3, 8e2, 'I', fontsize=16, color='magenta')
ax6.text( 25, 3e3, 'IV', fontsize=16, color='magenta')
ax6.text( 15, 3e2, 'V', fontsize=16, color='magenta')
ax6.text(100, 2e3, 'VI', fontsize=16, color='magenta')

ax6.set_yscale('log')
ax6.set_ylim([1,3e4])

ax6.set_xlabel('Time (Myr)')
ax6.set_ylabel('Atmospheric pressure (bar)')

# ---------------------------------------------------------------------------- #
plt.subplots_adjust(left=0.08, right=0.98, top=0.95, bottom=0.05, wspace=0.2, hspace=0.12)
plt.savefig('Plot_TR1_g_scenarios_evolution.png')
# plt.savefig('Plot_TR1_g_scenarios_evolution.pdf', format='pdf')
