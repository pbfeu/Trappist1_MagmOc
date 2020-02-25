import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable


# sns.set_style("whitegrid")
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
masses  = [0.766,0.926,1.14]
M_Earth = 5.972186e24 # Earth mass [kg]
TO      = 1.39e21     # mass of 1 Terr. Ocean [kg]

def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.))) / (np.sqrt(2*np.pi) * sig)


M_water = np.logspace(-2,3,num=100)  # Initial water mass [MO]
lw = len(M_water)

M_water_frac_e = np.zeros(lw)
M_water_frac_f = np.zeros(lw)
M_water_frac_g = np.zeros(lw)

for i in range(lw):
    M_water_frac_e[i] = M_water[i] * TO / (M_Earth * masses[0])
    M_water_frac_f[i] = M_water[i] * TO / (M_Earth * masses[0])
    M_water_frac_g[i] = M_water[i] * TO / (M_Earth * masses[0])


pdf_e = np.zeros((lw,2))
pdf_f = np.zeros((lw,2))
pdf_g = np.zeros((lw,2))

# Today's water mass fractions (Dorn et al., 2018), UCM
Water_Frac_e = 0.02
Water_Frac_f = 0.07
Water_Frac_g = 0.13

sig_e_up  = 0.015
sig_e_low = 0.015
sig_f     = 0.03
sig_g     = 0.04

Water_Mass_TO_e = Water_Frac_e * masses[0] * M_Earth / TO
Water_Mass_TO_f = Water_Frac_f * masses[1] * M_Earth / TO
Water_Mass_TO_g = Water_Frac_g * masses[2] * M_Earth / TO

sig_TO_e_up  = sig_e_up  * masses[0] * M_Earth / TO
sig_TO_e_low = sig_e_low * masses[0] * M_Earth / TO
sig_TO_f     = sig_f     * masses[1] * M_Earth / TO
sig_TO_g     = sig_g     * masses[2] * M_Earth / TO

for i in range(lw):
    if (M_water[i]<Water_Mass_TO_e):
        pdf_e[i,0] = gaussian(M_water[i], Water_Mass_TO_e, sig_TO_e_low)
    else:
        pdf_e[i,0] = gaussian(M_water[i], Water_Mass_TO_e, sig_TO_e_up)
    pdf_f[i,0] = gaussian(M_water[i], Water_Mass_TO_f, sig_TO_f)
    pdf_g[i,0] = gaussian(M_water[i], Water_Mass_TO_g, sig_TO_g)

    # if (M_water[i]<Water_Mass_TO_e):
    #     pdf_e[i,0] = gaussian(M_water_frac_e[i], Water_Frac_e, sig_e_low)
    # else:
    #     pdf_e[i,0] = gaussian(M_water_frac_e[i], Water_Frac_e, sig_e_up)
    # pdf_f[i,0] = gaussian(M_water_frac_f[i], Water_Frac_f, sig_f)
    # pdf_g[i,0] = gaussian(M_water_frac_g[i], Water_Frac_g, sig_g)

    pdf_e[i,1] = pdf_e[i,0]
    pdf_f[i,1] = pdf_f[i,0]
    pdf_g[i,1] = pdf_g[i,0]

    # print(M_water[i], pdf_e[i,0], pdf_f[i,0], pdf_g[i,0])

x_axis = [10001, 10002]

# plt.figure()
# plt.figure(num=None, figsize=(5, 9), dpi=300, facecolor='w', edgecolor='k')
# fig = plt.figure(num=None, figsize=(10, 9), dpi=300, facecolor='w', edgecolor='k')
fig = plt.figure(num=None, figsize=(3, 9), dpi=300, facecolor='w', edgecolor='k')

plt.plot(pdf_e[:,0], M_water, color=cmap(220))
plt.plot(pdf_f[:,0], M_water, color=cmap(200))
plt.plot(pdf_g[:,0], M_water, color=cmap(60))

plt.fill_betweenx(M_water, 1e-4, pdf_e[:,0], color=cmap(220), alpha=0.5)
plt.fill_betweenx(M_water, 1e-4, pdf_f[:,0], color=cmap(200), alpha=0.5)
plt.fill_betweenx(M_water, 1e-4, pdf_g[:,0], color=cmap(60), alpha=0.5)


plt.xscale('log')
plt.yscale('log')
plt.xlim([1e-4,1e-2])
plt.ylim([4e-2,1e3])
plt.tick_params(axis='y', which='both', direction='in')

# plt.xticklabels([])
# plt.xticklabels([])

plt.subplots_adjust(left=0.2, right=0.8, top=0.88, bottom=0.07, wspace=0.4, hspace=0.1)

plt.savefig('TR1_Water_Dorn_gaussian_new.png')


# plt.suptitle('Today\'s water content \n Dorn et al. (2018)', fontsize=18, fontweight='bold')
#
# #----------------------------------------------------------------------------------------------------------------- #
# ax3a = plt.subplot2grid((1,3), (0,0))
# ax3b = plt.subplot2grid((1,3), (0,1), sharex=ax3a, sharey=ax3a)
# ax3c = plt.subplot2grid((1,3), (0,2), sharex=ax3a, sharey=ax3a)
#
# pw_min = 0.0001
# pw_max = max(max(pdf_e[:,0]),max(pdf_f[:,0]),max(pdf_g[:,0]))
#
# ca = ax3a.pcolor(x_axis, M_water, pdf_e,   cmap='Greys', vmin=pw_min, vmax=pw_max, norm=mpl.colors.LogNorm())
# cb = ax3b.pcolor(x_axis, M_water, pdf_f,   cmap='Greys', vmin=pw_min, vmax=pw_max, norm=mpl.colors.LogNorm())
# cc = ax3c.pcolor(x_axis, M_water, pdf_g,   cmap='Greys', vmin=pw_min, vmax=pw_max, norm=mpl.colors.LogNorm())
# ax3a.grid(color='grey', which='major', axis='y', linestyle='-',)
# ax3b.grid(color='grey', which='major', axis='y', linestyle='-',)
# ax3c.grid(color='grey', which='major', axis='y', linestyle='-',)
#
# ax3a.set_title('e')
# ax3b.set_title('f')
# ax3c.set_title('g')
#
# ax3a.set_yscale('log')
# ax3b.set_yticklabels([])
# ax3c.set_yticklabels([])
# ax3a.set_xticklabels([])
# ax3b.set_xticklabels([])
# ax3c.set_xticklabels([])
#
# # divider = make_axes_locatable(ax3c)
# # cax = divider.append_axes('right', size='20%', pad=0.05)
# # cbar = plt.colorbar(cc, cax=cax, orientation='vertical')
# # cbar.set_label('Probability Distribution', rotation=270, labelpad=20,fontsize=16, fontweight='bold')
#
# # ax3a.set_xlabel('Eccentricity')
# # ax3a.set_ylabel('VPLanet (grey)')
#
# ax3a.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# ax3b.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# ax3c.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# ax3a.set_ylim([4e-2,1e3])

# ----------------------------------------------------------------------------------------------------------------- #
# plt.tight_layout()
# plt.subplots_adjust(left=0.08, right=0.98, top=0.88, bottom=0.07)#, wspace=0.23, hspace=0.1)

# plt.subplots_adjust(left=0.2, right=0.8, top=0.88, bottom=0.07, wspace=0.4, hspace=0.1)
# plt.savefig('TR1_Water_Dorn.png')
# plt.show()
