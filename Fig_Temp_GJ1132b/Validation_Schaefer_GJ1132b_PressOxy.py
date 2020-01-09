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
Water_grey = [0.1, 85, 90, 95, 100] # in Myr, no escape
Oxy_grey   = [  0,  0, 30, 68, 107] # in Myr, XUV-abs eff. = 0.15

Water_petit = [0.1, 130, 135, 140, 150,  200] # in Myr, XUV-abs eff. = 0.3
Oxy_petit   = [  0,   0,  12,  71, 241, 2844]

# Results from Schaefer et al. (2016), Figure 7a
SchaeferWater = [ 100,222,254,306,341,806,985,1131,1249,1356]
SchaeferOxy   = [0,1e-5,1e-4,1e-3,1e-2,1e-1,1e0,1e1,1e2,1e3]

# -- Plot -- #
plt.figure(num=None, figsize=(8, 6), dpi=300, facecolor='w', edgecolor='k')
plt.title('GJ1132b: oxygen pressure at magma ocean solidification', fontsize=16, fontweight='bold')

## Colors
plt.plot(Water_grey, Oxy_grey, label='VPLanet (grey)', color=cmap(200), linewidth=3.0)
plt.plot(Water_petit, Oxy_petit, label='VPLanet (petit)', color=cmap(220), linewidth=3.0)
plt.plot(SchaeferWater, SchaeferOxy, label='Schaefer (XUV-Model A)', color='b', linewidth=3.0)

## Black & white
# plt.plot(WaterFracIni, SolidTime_00, label='VPLanet (no escape)', marker='^', color=cmap(0), linewidth=3.0, linestyle=':')
# plt.plot(WaterFracIni, SolidTime_15, label='VPLanet ($\\epsilon_{XUV} = 0.15$)', marker='v', color=cmap(0), linewidth=3.0, linestyle='--')
# plt.plot(WaterFracIni, SolidTime_30, label='VPLanet ($\\epsilon_{XUV} = 0.3$)', marker='o', color=cmap(0), linewidth=3.0)
# plt.plot(SchaeferWater, SchaeferA, label='Schaefer XUV-Model A', color='grey', linewidth=3.0)
# plt.plot(SchaeferWater, SchaeferB, label='Schaefer XUV-Model B', color='grey', linewidth=3.0, linestyle='--')

plt.legend(loc='best', frameon=True, fontsize=14)
plt.xlabel('Initial Water Mass (TO)', fontsize=14, fontweight='bold')
plt.ylabel('Oxygen pressure (bar)', fontsize=14, fontweight='bold')
plt.xlim([80,1500])
plt.ylim([1e-5,1e4])
plt.xscale('log')
plt.yscale('log')
plt.tick_params(labelsize=13)
plt.tight_layout()
plt.savefig('OxyPress_Validation_Schaefer_GJ1132b.png')
