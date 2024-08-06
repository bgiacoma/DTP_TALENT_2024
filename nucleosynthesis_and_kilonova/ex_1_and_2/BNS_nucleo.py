## Main script for nucleosynthesis analysis

import numpy as np
import nsys_yields as nsys
import parameters  as pars
import h5py
import matplotlib.pyplot as plt

#===================================================
# choose one of the two simulations
#sim = 'DD2_M13641364_M0_SR'
sim = 'SFHo_M11461635_M0_LK_SR'

# choose one of the two criteria
crit_unbound = 'geo'
#crit_unbound = 'bern'
#===================================================

print('I am considering the following simulation:', sim)
print('I am considering the following criterion:', crit_unbound)


## Make convolution with SkyNet data
nsys.compute_yields(sim,crit_unbound)

print('I am reading the abundances from the simulation')
hist_folder = pars.data_folder+sim+'/nucleosynthesis_'+crit_unbound+'/'+pars.crit_tau+'/'

hf = h5py.File(hist_folder+'abundances.h5','r')
A_array = np.array(hf.get('A'))
Z_array = np.array(hf.get('Z'))
costh_array = np.array(hf.get('costh'))
yields_Y_A = np.array(hf.get('yields_A'))
yields_Y_Z = np.array(hf.get('yields_Z'))
m_ejecta = np.array(hf.get('m_ejecta'))
hf.close()

print('I am reading the mass fractions from the simulations')
hist_folder = pars.data_folder+sim+'/nucleosynthesis_'+crit_unbound+'/'+pars.crit_tau+'/'

hf = h5py.File(hist_folder+'mass_fractions.h5','r')
A_array = np.array(hf.get('A'))
Z_array = np.array(hf.get('Z'))
costh_array = np.array(hf.get('cos_thetas'))
yields_X_A = np.array(hf.get('yields_A'))
yields_X_Z = np.array(hf.get('yields_Z'))
m_ejecta = np.array(hf.get('m_ejecta'))
hf.close()

print(costh_array)

#===================================================
# here I am selecting one polar angle
ith=12
print('I am considering the polar angle:',np.arccos(costh_array[ith])*180/3.14159)

# plotting part
nnrows = 1
nncols = 1
fig, ax = plt.subplots(nrows=nnrows, ncols=nncols,figsize=(4,3),sharex=True,sharey=True)

ax.scatter(A_array,yields_Y_A[:,ith])
ax.set_ylim([1.e-8,1.e-1])
ax.set_yscale('log')
#===================================================

plt.show()



