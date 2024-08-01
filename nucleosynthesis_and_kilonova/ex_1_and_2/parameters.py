## Define parameters for nucleosynthesis analysis

import numpy as np

## Data folder
data_folder = "./THC_data/"

############################
# NR simulation parameters #
############################

## Criterion to select the ejecta
crit_unbound = 'geo'
#       geo   for the geodesic criterion
#       bern  for the Bernoulli criterion

## Criterion to compute the expansion timescale
crit_tau = 'density_based'
#       radius_based  to compute tau by dividing characteristic radius by the asymptotic velocity (tau=300./v_inf)
#       density_based to compute tau by matching homologous expansion of the ejecta with SkyNet density history (tau=(rho_E/rho(s,Ye,T=8GK))**(1/3)*(e/3)*(r_E/v_inf))

## Define bins for ejecta in (s,Ye,tau) space
# entropy [kB/baryon]
min_entr = 1.5
max_entr = 300.
log_entr = True #True for logarithmic, False for linear spacing

# ye
min_ye = 0.01
max_ye = 0.48
log_ye = False

# tau [ms]
min_tau = 0.5
max_tau = 200.
log_tau = True

## Define eventual cut for ejecta properties
cut_entr = False
cut_entr_lim = [min_entr, max_entr]

cut_ye = False
cut_ye_lim = [min_ye, max_ye]

cut_tau = False
cut_tau_lim = [min_tau, max_tau]

#####################
# SkyNet parameters #
#####################

## SkyNet data folder
SN_folder = './SkyNet_data/'

## SkyNet Y/X data
SN_Y_file = 'skynet_data_Y_A_Z.h5'
SN_X_file = 'skynet_data_X_A_Z.h5'

