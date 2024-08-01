
import numpy as np
import os
import h5py
import NR_outflow  as NR


#===================================================
# choose one of the two simulations
#sim = 'DD2_M13641364_M0_SR'
sim = 'SFHo_M11461635_M0_LK_SR'

# choose one of the two criteria
#crit_unbound = 'geo'
crit_unbound = 'bern'
#===================================================

print(' ')
print('I am considering the following simulation:', sim)
print('I am considering the following criterion:', crit_unbound)

# Read ejecta histogram
[costh, bins_tau, bins_entr, bins_ye, H, m_ejecta] = NR.read_hist(sim,crit_unbound)

print(' ')
print('size of the costh array:',np.shape(costh))
print('costh array:',costh)
print(' ')
print('size of tau array',np.shape(bins_tau))
print('tau array',bins_tau)
print(' ')
print('size of entropy array',np.shape(bins_entr))
print('entr array',bins_entr)
print(' ')
print('size of ye array',np.shape(bins_ye))
print('ye array',bins_ye)
print(' ')
print('ejecta mass in every angular bin',m_ejecta)
print(' ')
print('shape of the histogram:',np.shape(H))
print(' ')
