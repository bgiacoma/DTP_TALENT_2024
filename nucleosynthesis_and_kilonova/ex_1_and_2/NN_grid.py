## Compute convolution between ejecta histograms and SkyNet data

import SkyNet_data as SN_data
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker, cm

# select one option
#==================================================
tau_fix = False
tau     = 10.          # tau in ms

s_fix   = True
s       = 200.          # s in kb/baryon

ye_fix  = False         
ye      = 0.1          # ye
#==================================================


## Read SkyNet data (nuclides, abundances, mass fractions)
print("Reading SkyNet data...")
[A,Z,s_array,tau_array,ye_array,YA_tau_s_ye,YZ_tau_s_ye] = SN_data.read_SN_Y_data()
[A,Z,s_array,tau_array,ye_array,XA_tau_s_ye,XZ_tau_s_ye] = SN_data.read_SN_X_data()
print("Done!\n")

print('shape of A array:',np.shape(A))
print('A array',A)
print(' ')
print('shape of Z array:',np.shape(Z))
print('Z array',Z)
print(' ')
print('shape of s array:',np.shape(s_array))
print('s array',s_array)
print(' ')
print('shape of tau array:',np.shape(tau_array))
print('tau array',tau_array)
print(' ')
print('shape of ye array:',np.shape(ye_array))
print('tau array',ye_array)
print(' ')
print('shape of abundance table',np.shape(YA_tau_s_ye))
print('shape of mass fraction table',np.shape(XA_tau_s_ye))
print(' ')

# get the array dimensions
nA1,nA2,nA3,nA4 = YA_tau_s_ye.shape
nZ1,nZ2,nZ3,nZ4 = YZ_tau_s_ye.shape

# define two arrays, same size as YA_tau_s_ye
# and YZ_tau_s_ye, but containing many copies of the A and Z 1D arrays
testZ = np.array([Z,]*(nZ1*nZ2*nZ3)).reshape(nZ1,nZ2,nZ3,nZ4)
testA = np.array([A,]*(nA1*nA2*nA3)).reshape(nA1,nA2,nA3,nA4)

#==================================================================
# Example: prepare Hydrogen abundances
Zspec = 1
tmpZ = np.where( testZ==Zspec, YZ_tau_s_ye, 0.)
print(np.shape(tmpZ))
#==================================================================

Y_to_plot = np.sum(tmpZ,axis=3)

# build the grid for the plot

if (tau_fix):
    X, Y = np.meshgrid(ye_array, s_array)
    itau = np.argmin(abs(tau_array-tau))
    Z = Y_to_plot[itau,:,:]
    print('I am considering trajectories at tau='+str(tau_array[itau])+' ms')
    
if (s_fix):
    X, Y = np.meshgrid(ye_array, tau_array)
    ientr = np.argmin(abs(s_array-s))
    Z = Y_to_plot[:,ientr,:]
    print('I am considering trajectories at s='+str(s_array[ientr])+' kB/baryon')

if (ye_fix):
    X, Y = np.meshgrid(s_array, tau_array)
    iye = np.argmin(abs(ye_array-ye))
    Z = Y_to_plot[:,:,iye]
    print('I am considering trajectories at Ye='+str(ye_array[iye]))


nnrows = 1
nncols = 1
fig, ax = plt.subplots(nrows=nnrows, ncols=nncols,figsize=(4,3),sharex=True,sharey=True)

# set the plot levels
levels = [1.e-4,1.e-3,1.e-2,1.e-1]#np.arange(-5, 0.25, 1)
levels1 = np.logspace(np.log10(1.e-5), np.log10(1.e-1),1000)

# color-coded abundances
cs = ax.contourf(X, Y, Z,locator=ticker.LogLocator(),levels=levels1,extend='both',cmap='viridis')

if (tau_fix):
    ax.set_yscale('log')
    ax.set_xlim([0.02,0.48])
    ax.set_xlabel('${Y_e}$', fontsize=16)
    ax.set_ylabel(r'${s} \, [k_{\rm B}~{\rm baryon^{-1}}]$', fontsize=16)
    ax.text(0.2,450,r"Abundances at 30 years for $\tau$ = "+str(tau_array[itau])+" ms trajectories", fontsize=16)


if (s_fix):
    ax.set_yscale('log')
    ax.set_xlim([0.02,0.48])
    ax.set_xlabel('${Y_e}$', fontsize=16)
    ax.set_ylabel(r'${\tau} \, [ms]$', fontsize=16)
    ax.text(0.2,250,r"Abundances at 30 years for s = "+str(s_array[ientr])+" kb/baryon trajectories", fontsize=16)

if (ye_fix):
    ax.set_xscale('log')
    ax.set_yscale('log')
    #ax.set_xlim([0.02,0.48])
    ax.set_ylabel(r'${\tau} \, [ms]$', fontsize=16)
    ax.set_xlabel(r'${s} \, [k_{\rm B}~{\rm baryon^{-1}}]$', fontsize=16)
    ax.text(5,250,r"Abundances at 30 years for ye = "+str(ye_array[iye])+" trajectories", fontsize=16)

ax.tick_params(axis='both',direction="in", which='both',color='w')
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')
ax.grid(ls='--',alpha=0.4)

cbar = fig.colorbar(cs,ticks=levels,spacing='uniform',orientation='vertical')#,ax=ax.ravel().tolist(),pad=0.02)
cax = cbar.ax

#plt.savefig(output_folder+'const_tau_'+str(tau_array[id_tau])+'_time_'+str(time_array[id_time])+'.png',dpi=600,bbox_inches='tight')


plt.show()
