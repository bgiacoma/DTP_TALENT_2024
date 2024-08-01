## Compute convolution between ejecta histograms and SkyNet data

import numpy as np
import os
import h5py
import SkyNet_data as SN_data
import NR_outflow  as NR
import parameters  as pars

## Read SkyNet data (nuclides, abundances, mass fractions)
print("Reading SkyNet data...")
[A, Z] = SN_data.read_nuclides()
[fyields_Y_A, fyields_Y_Z] = SN_data.read_and_interpolate_SN_Y_data()
[fyields_X_A, fyields_X_Z] = SN_data.read_and_interpolate_SN_X_data()
print("Done!\n")


## Compute the yields in BNS ejecta vs t, A/Z, theta
def compute_yields(sim,crit_unbound):

    hist_folder = pars.data_folder+sim+'/nucleosynthesis_'+crit_unbound+'/'+pars.crit_tau+'/'

    print("Computing convolution for: "+sim+"  using ejecta from "+crit_unbound+" criterion.")	

    # Read ejecta histogram
    [costh, bins_tau, bins_entr, bins_ye, H, m_ejecta] = NR.read_hist(sim,crit_unbound)

    nbin_tau  = np.shape(bins_tau)[0]
    nbin_entr = np.shape(bins_entr)[0]
    nbin_ye   = np.shape(bins_ye)[0]

    # Define the arrays for the yields
    # number abundances
    yields_Y_A = []
    yields_Y_Z = []

    # mass fractions
    yields_X_A = [] 
    yields_X_Z = [] 

    # Reshape ejecta histogram with shape of SkyNet data
    mesh = np.array(np.meshgrid(bins_tau,bins_entr,bins_ye,indexing='ij')).T.reshape(-1,3)

    Y_At = [] 
    Y_Zt = []
    
    X_At = [] 
    X_Zt = []

    # Loop over the atomic numbers
    # number abundances        
    yields_Y_Z = np.array([convolution(nbin_tau,nbin_entr,nbin_ye,fyields_Y_Z[iZ](mesh),H,m_ejecta) for iZ,_ in enumerate(Z)])
    	
    # mass fractions
    yields_X_Z = np.array([convolution(nbin_tau,nbin_entr,nbin_ye,fyields_X_Z[iZ](mesh),H,m_ejecta) for iZ,_ in enumerate(Z)])

    # Loop over the mass numbers
    # number abundances        
    yields_Y_A = np.array([convolution(nbin_tau,nbin_entr,nbin_ye,fyields_Y_A[iA](mesh),H,m_ejecta) for iA,_ in enumerate(A)])
    
    # mass fractions
    yields_X_A = np.array([convolution(nbin_tau,nbin_entr,nbin_ye,fyields_X_A[iA](mesh),H,m_ejecta) for iA,_ in enumerate(A)])
    
    #yields_Y_A = np.array(yields_Y_A)
    #yields_Y_Z = np.array(yields_Y_Z)  
          
    #yields_X_A = np.array(yields_X_A)
    #yields_X_Z = np.array(yields_X_Z)  

    ## Create HDF5 dataset
    # number abundances
    hf = h5py.File(hist_folder+'abundances.h5','w')
    hf.create_dataset('A',data=A)
    hf.create_dataset('Z',data=Z)
    hf.create_dataset('cos_thetas',data=costh)
    hf.create_dataset('yields_A',data=yields_Y_A)
    hf.create_dataset('yields_Z',data=yields_Y_Z)
    hf.create_dataset('m_ejecta',data=m_ejecta)
    hf.close()

    # mass fractions
    hf = h5py.File(hist_folder+'mass_fractions.h5','w')
    hf.create_dataset('A',data=A)
    hf.create_dataset('Z',data=Z)
    hf.create_dataset('cos_thetas',data=costh)
    hf.create_dataset('yields_A',data=yields_X_A)
    hf.create_dataset('yields_Z',data=yields_X_Z)
    hf.create_dataset('m_ejecta',data=m_ejecta)
    hf.close()

    print("All done!\n")
    return


## Make the convolution
def convolution(nbin_tau,nbin_entr,nbin_ye,fyields, H, m_ejecta):
    #print(np.shape(fyields))
    tmp = np.array([fyields.reshape((nbin_tau,nbin_entr,nbin_ye),order='F')] * NR.ntheta)
    #print(np.shape(tmp))
    #print(np.shape(H))
    conv = np.sum(np.sum(np.sum(tmp * H, axis=1), axis=1), axis=1) / m_ejecta
    return conv
