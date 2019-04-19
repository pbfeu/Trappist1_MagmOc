import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread
import seaborn as sns

sns.set_style("whitegrid")
plt.close('all')

cmap=plt.get_cmap('nipy_spectral')
plt.close('all')

WaterFracIni  = [0.0014,0.014,0.14,1.4] # in weight percent
StartSolid    = [2e-4, 0.651] # in Myr
SwitchLowPres = [0.0644, 10.296] # in Myr
SolidTime_00  = [0.0453, 0.5173, 4.9161, 57.09] # in Myr, no escape
SolidTime_15  = [0.0097, 0.0973, 1.0724, 32.65] # in Myr, XUV-abs eff. = 0.15
SolidTime_30  = [0.0051, 0.0405, 0.4988, 18.10] # in Myr, XUV-abs eff. = 0.3

WaterFracIni_petit = 1.4
SolidTime_30_petit = [, , , 27.995]

SchaeferWater = [ 10**-2.7,10**-1.7,  10**-1, 10**-0.7,10**-0.01,10**0.69,  10**1,10**1.27]
SchaeferB     = [10**-1.65,10**0.32,10**1.15, 10**1.45, 10**2.18, 10**2.9,10**3.7,10**3.7]
SchaeferA     = [10**-2.26,10**-1.3,10**-0.6,10**-0.28,10**0.823, 10**2.6,10**3.1,10**3.7]

plt.title('Magma Ocean solidification time of GJ1132b', fontsize=16, fontweight='bold')

# Colors
plt.plot(WaterFracIni, SolidTime_00, label='VPLanet ($\\epsilon_{XUV} = 0$)', marker='^', color=cmap(200), linewidth=3.0)
plt.plot(WaterFracIni, SolidTime_15, label='VPLanet ($\\epsilon_{XUV} = 0.15$)', marker='v', color=cmap(220), linewidth=3.0)
plt.plot(WaterFracIni, SolidTime_30, label='VPLanet ($\\epsilon_{XUV} = 0.3$)', marker='o', color=cmap(120), linewidth=3.0)
plt.plot(WaterFracIni_petit, SolidTime_30_petit, label='VPLanet ($petitCODE$)', marker='p', color=cmap(10), linewidth=3.0)
plt.plot(SchaeferWater, SchaeferA, label='Schaefer XUV-Model A', color='b', linewidth=3.0)
plt.plot(SchaeferWater, SchaeferB, label='Schaefer XUV-Model B', color='magenta', linewidth=3.0)

# Black
# plt.plot(WaterFracIni, SolidTime_00, label='VPLanet ($\\epsilon_{XUV} = 0$)', marker='^', color=cmap(0), linewidth=3.0, linestyle=':')
# plt.plot(WaterFracIni, SolidTime_15, label='VPLanet ($\\epsilon_{XUV} = 0.15$)', marker='v', color=cmap(0), linewidth=3.0, linestyle='--')
# plt.plot(WaterFracIni, SolidTime_30, label='VPLanet ($\\epsilon_{XUV} = 0.3$)', marker='o', color=cmap(0), linewidth=3.0)
# plt.plot(WaterFracIni_petit, SolidTime_30_petit, label='VPLanet ($petitCODE$)', marker='p', color=cmap(0), linewidth=3.0)
# plt.plot(SchaeferWater, SchaeferA, label='Schaefer XUV-Model A', color='grey', linewidth=3.0)
# plt.plot(SchaeferWater, SchaeferB, label='Schaefer XUV-Model B', color='grey', linewidth=3.0, linestyle='--')

plt.legend(loc='best', frameon=True, fontsize=14)
plt.xlabel('Initial Water Mass Fraction (wt%)', fontsize=14, fontweight='bold')
plt.ylabel('Solidification Time (Myr)', fontsize=14, fontweight='bold')
plt.xlim([1e-3,1e2])
plt.ylim([1e-3,1e4])
plt.xscale('log')
plt.yscale('log')
plt.tick_params(labelsize=13)
plt.show()
