## Histogram of Numerical Relativity simulation outflow

import numpy as np
#import numpy.ma as ma
#import os
#import sys
import h5py
#import math
#import gc
#import EOS
#import units
#import SkyNet_data as SN_data
import parameters  as pars

#import warnings
#warnings.filterwarnings("ignore", category=RuntimeWarning) 


## Useful numbers
n2theta = 51
ntheta  = 26 #half theta values
nphi    = 93

## Read ejecta histogram
def read_hist(sim,crit_unbound):

    hist_folder = pars.data_folder+sim+'/nucleosynthesis_'+crit_unbound+'/'+pars.crit_tau+'/'
	
    hf = h5py.File(hist_folder+'histograms_light.h5','r')
    costh      = np.array(hf.get('cos_thetas'))
    bins_tau   = np.array(hf.get('bins_tau'))
    bins_entr  = np.array(hf.get('bins_entr'))
    bins_ye    = np.array(hf.get('bins_ye'))
    H          = np.array(hf.get('histograms'))
    m_ejecta   = np.array(hf.get('m_ejecta'))
    hf.close()

    return [costh, bins_tau, bins_entr, bins_ye, H, m_ejecta]
