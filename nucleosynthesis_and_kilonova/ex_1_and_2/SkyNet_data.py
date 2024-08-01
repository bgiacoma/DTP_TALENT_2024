## Routines for reading and interpolating SkyNet data

import numpy as np
import h5py
from scipy.interpolate import RegularGridInterpolator
import parameters as pars
   

## Interpolate SkyNet abundances/mass fraction in (tau,s,ye) space
def interpolate_SN_yields(A,SN_A_t_tau_s_ye):
    # Read SkyNet grid
    hf = h5py.File(pars.SN_folder+pars.SN_Y_file,'r')
    s_array   = np.array(hf.get('s'))
    ye_array  = np.array(hf.get('ye'))
    tau_array = np.array(hf.get('tau'))
    hf.close()

    fyields = []

    # Loop over Z/A values
    for iA,_ in enumerate(A): #here A can be either the mass number or the atomic number
       func = RegularGridInterpolator((tau_array, s_array, ye_array),SN_A_t_tau_s_ye[:,:,:,iA])
       fyields.append(func)

    return fyields
   

## Read and interpolate SkyNet initial density 
def read_and_interpolate_SN_rho():
    # Read SkyNet grid
    hf = h5py.File(pars.SN_folder+pars.SN_rhofile,'r')
    s_array   = np.array(hf.get('s'))
    ye_array  = np.array(hf.get('ye'))
    rho_s_ye = np.array(hf.get('rho_s_ye'))
    hf.close()

    # Interpolate in (s,Ye) space
    rho_h5_dat = RegularGridInterpolator((s_array, ye_array),rho_s_ye[:,:],bounds_error=False,fill_value=None)
    return rho_h5_dat


## Read and interpolate SkyNet number abundances
def read_and_interpolate_SN_Y_data():
    hf = h5py.File(pars.SN_folder+pars.SN_Y_file,'r')
    YAt_tau_s_ye = np.array(hf.get('Y_A_t_tau_s_ye'))
    YZt_tau_s_ye = np.array(hf.get('Y_Z_t_tau_s_ye'))
    A  = np.array(hf.get('A'))
    Z  = np.array(hf.get('Z'))
    hf.close()

    # Interpolate in (tau,s,Ye) space
    fyields_A = interpolate_SN_yields(A,YAt_tau_s_ye)
    fyields_Z = interpolate_SN_yields(Z,YZt_tau_s_ye)

    return [fyields_A, fyields_Z]


## Read and interpolate SkyNet mass fractions
def read_and_interpolate_SN_X_data():
    hf = h5py.File(pars.SN_folder+pars.SN_X_file,'r')
    XAt_tau_s_ye = np.array(hf.get('X_A_t_tau_s_ye'))
    XZt_tau_s_ye = np.array(hf.get('X_Z_t_tau_s_ye'))
    A  = np.array(hf.get('A'))
    Z  = np.array(hf.get('Z'))
    hf.close()

    # Interpolate in (tau,s,Ye) space
    fyields_A = interpolate_SN_yields(A,XAt_tau_s_ye)
    fyields_Z = interpolate_SN_yields(Z,XZt_tau_s_ye)

    return [fyields_A, fyields_Z]


## Read SkyNet A/Z nuclides
def read_nuclides():
    hf = h5py.File(pars.SN_folder+pars.SN_Y_file,'r')
    A  = np.array(hf.get('A'))
    Z  = np.array(hf.get('Z'))
    hf.close()

    return [A, Z]

## Read SkyNet number abundances
def read_SN_Y_data():
    hf = h5py.File(pars.SN_folder+pars.SN_Y_file,'r')
    YAt_tau_s_ye = np.array(hf.get('Y_A_t_tau_s_ye'))
    YZt_tau_s_ye = np.array(hf.get('Y_Z_t_tau_s_ye'))
    A  = np.array(hf.get('A'))
    Z  = np.array(hf.get('Z'))
    s_array   = np.array(hf.get('s'))
    ye_array  = np.array(hf.get('ye'))
    tau_array = np.array(hf.get('tau'))
    hf.close()

    return [A,Z,s_array,tau_array,ye_array,YAt_tau_s_ye,YZt_tau_s_ye]


## Read SkyNet mass fractions
def read_SN_X_data():
    hf = h5py.File(pars.SN_folder+pars.SN_X_file,'r')
    XAt_tau_s_ye = np.array(hf.get('X_A_t_tau_s_ye'))
    XZt_tau_s_ye = np.array(hf.get('X_Z_t_tau_s_ye'))
    A  = np.array(hf.get('A'))
    Z  = np.array(hf.get('Z'))
    s_array   = np.array(hf.get('s'))
    ye_array  = np.array(hf.get('ye'))
    tau_array = np.array(hf.get('tau'))
    hf.close()

    return [A,Z,s_array,tau_array,ye_array,XAt_tau_s_ye,XZt_tau_s_ye]

