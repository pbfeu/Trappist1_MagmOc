#############################################
#   Validation of the results for GJ1132b   #
#        from Schaefer et al. (2016)        #
#           with the VPLanet code           #
#       Used modules: MagmOc & AtmEsc       #
#############################################

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
cmap=plt.get_cmap('nipy_spectral')
plt.close('all')

WaterFracIni  = [0.0014,0.014,0.14,1.4] # in weight percent, corresponds to 0.1,1,10,100 terrestrial oceans

# Results for GJ1132b with VPLanet
SolidTime_00  = [  25.5,  30.7, 34.8, 70.7] # in Myr, no escape
SolidTime_15  = [0.0097, 0.098, 1.06, 53.0] # in Myr, XUV-abs eff. = 0.15
SolidTime_30  = [0.0049, 0.049, 0.50, 27.6] # in Myr, XUV-abs eff. = 0.3

# Results from Schaefer et al. (2016), Figure 5
SchaeferWater = [ 10**-2.7,10**-1.7,  10**-1, 10**-0.7,10**-0.01,10**0.69,  10**1,10**1.27]
SchaeferB     = [10**-1.65,10**0.32,10**1.15, 10**1.45, 10**2.18, 10**2.9,10**3.7, 10**3.7]
SchaeferA     = [10**-2.26,10**-1.3,10**-0.6,10**-0.28,10**0.823, 10**2.6,10**3.1, 10**3.7]

# -- Plot -- #
plt.figure(num=None, figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
plt.title('Magma Ocean solidification time of GJ1132b', fontsize=16, fontweight='bold')

## Colors
plt.plot(WaterFracIni, SolidTime_00, label='VPLanet (no escape)', marker='^', color=cmap(200), linewidth=3.0)
plt.plot(WaterFracIni, SolidTime_15, label='VPLanet ($\\epsilon_{XUV} = 0.15$)', marker='v', color=cmap(220), linewidth=3.0)
plt.plot(WaterFracIni, SolidTime_30, label='VPLanet ($\\epsilon_{XUV} = 0.3$)', marker='o', color=cmap(120), linewidth=3.0)
plt.plot(SchaeferWater, SchaeferA, label='Schaefer XUV-Model A', color='b', linewidth=3.0)
plt.plot(SchaeferWater, SchaeferB, label='Schaefer XUV-Model B', color='magenta', linewidth=3.0)

## Black & white
# plt.plot(WaterFracIni, SolidTime_00, label='VPLanet (no escape)', marker='^', color=cmap(0), linewidth=3.0, linestyle=':')
# plt.plot(WaterFracIni, SolidTime_15, label='VPLanet ($\\epsilon_{XUV} = 0.15$)', marker='v', color=cmap(0), linewidth=3.0, linestyle='--')
# plt.plot(WaterFracIni, SolidTime_30, label='VPLanet ($\\epsilon_{XUV} = 0.3$)', marker='o', color=cmap(0), linewidth=3.0)
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
plt.tight_layout()
plt.savefig('Validation_Schaefer_GJ1132b.png')
