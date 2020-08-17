import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

plt.close('all')

cmap=plt.get_cmap('nipy_spectral')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.color'] = cmap(0)
mpl.rcParams['axes.labelsize'] = 14
mpl.rcParams['axes.titlesize'] = 16
mpl.rcParams['xtick.labelsize'] = 13
mpl.rcParams['ytick.labelsize'] = 13
mpl.rcParams['legend.fontsize'] = 14
mpl.rcParams['axes.titleweight'] = 'bold'


planets = ['e','f','g']
masses  = np.array([0.766,0.926,1.14])
M_Earth = 5.972186e24 # Earth mass [kg]
TO      = 1.39e21     # mass of 1 Terr. Ocean [kg]

factor  = TO / (M_Earth * masses)

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / (np.sqrt(2*np.pi) * sig)


M_water = np.logspace(-2,4,num=500)  # Initial water mass [MO]
lw = len(M_water)

M_water_frac_e = np.zeros(lw)
M_water_frac_f = np.zeros(lw)
M_water_frac_g = np.zeros(lw)

for i in range(lw):
    M_water_frac_e[i] = M_water[i] * TO / (M_Earth * masses[0])
    M_water_frac_f[i] = M_water[i] * TO / (M_Earth * masses[0])
    M_water_frac_g[i] = M_water[i] * TO / (M_Earth * masses[0])

pdf_e = np.zeros(lw)
pdf_f = np.zeros(lw)
pdf_g = np.zeros(lw)

# Today's water mass fractions (Dorn et al., 2018), UCM
Water_Frac_e = 0.02
Water_Frac_f = 0.07
Water_Frac_g = 0.13

sig_e_up  = 0.015
sig_e_low = 0.015
sig_f     = 0.03
sig_g     = 0.04

for i in range(lw):
    if (M_water_frac_e[i]<Water_Frac_e):
        pdf_e[i] = gaussian(M_water_frac_e[i], Water_Frac_e, sig_e_low)
    else:
        pdf_e[i] = gaussian(M_water_frac_e[i], Water_Frac_e, sig_e_up)
    pdf_f[i] = gaussian(M_water_frac_f[i], Water_Frac_f, sig_f)
    pdf_g[i] = gaussian(M_water_frac_g[i], Water_Frac_g, sig_g)

fig = plt.figure(num=None, figsize=(2, 9), dpi=300, facecolor='w', edgecolor='k')
fig.suptitle('Dorn et al.\n(2018)', fontsize=18, fontweight='bold')

plt.plot(pdf_e, M_water_frac_e, color=cmap(220))
plt.plot(pdf_f, M_water_frac_f, color=cmap(200))
plt.plot(pdf_g, M_water_frac_g, color=cmap(60))

plt.fill_betweenx(M_water_frac_e, 1e-4, pdf_e, color=cmap(220))
plt.fill_betweenx(M_water_frac_f, 1e-4, pdf_f, color=cmap(200))
plt.fill_betweenx(M_water_frac_g, 1e-4, pdf_g, color=cmap(60))


plt.xscale('log')
plt.yscale('log')
plt.xlim([0.3,30])
plt.ylim([1e-5,1])
plt.tick_params(axis='y', which='both', direction='in')

plt.subplots_adjust(left=0.3, right=0.9, top=0.88, bottom=0.07, wspace=0.4, hspace=0.1)

# plt.savefig('TR1_Water_Dorn_fraction.png')
plt.savefig('TR1_Water_Dorn_fraction.eps', format='eps')
