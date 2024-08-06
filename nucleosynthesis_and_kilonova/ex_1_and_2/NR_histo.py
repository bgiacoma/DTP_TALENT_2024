
import numpy as np
import os
import h5py
import NR_outflow  as NR
import matplotlib.pyplot as plt

#===================================================
# choose one of the two simulations
sim = 'DD2_M13641364_M0_SR'
#sim = 'SFHo_M11461635_M0_LK_SR'

# choose one of the two criteria
#crit_unbound = 'geo'
crit_unbound = 'bern'
#===================================================

nnrows = 1
nncols = 3

fig, axs = plt.subplots(nrows=nnrows, ncols=nncols,figsize=(16,4),sharex=True,sharey=False)


sims=['DD2_M13641364_M0_SR','SFHo_M11461635_M0_LK_SR']
crits = ['geo','bern']

for sim in sims:
 
    for crit_unbound in crits:

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
        
        #nnrows = 1
        #nncols = 3
        
        #fig, axs = plt.subplots(nrows=nnrows, ncols=nncols,figsize=(16,4),sharex=True,sharey=False)
        
        
        # let's start with entropy...
        # loop over the angles
        avg = []
        for ith in range(np.shape(costh)[0]):
            tmp=np.sum(np.sum(H[ith,:,:,:],axis=2),axis=0)
            tmp2 = tmp*bins_entr/m_ejecta[ith]
            avg.append(np.sum(tmp2))
        
        avg = np.asarray(avg)
        axs[0].plot(np.arccos(costh)*180/3.14159,avg)
        axs[0].set_xlabel(r'$\theta$')
        axs[0].set_ylabel(r'$\langle s \rangle$')
        axs[0].set_yscale('log')
        axs[0].set_ylim([1,100.])
        #plt.title('entropy')
        
        
        # let's go with Ye...
        # loop over the angles
        avg = []
        for ith in range(np.shape(costh)[0]):
            tmp=np.sum(np.sum(H[ith,:,:,:],axis=1),axis=0)
            tmp2 = tmp*bins_ye/m_ejecta[ith]
            avg.append(np.sum(tmp2))
        
        avg = np.asarray(avg)
        axs[1].plot(np.arccos(costh)*180/3.14159,avg)
        axs[1].set_xlabel(r'$\theta$')
        axs[1].set_ylabel(r'$\langle Y_e \rangle$')
        #axs[1].set_yscale('log')
        axs[1].set_ylim([0.01,0.5])
        
        #plt.title('electron fraction')
        
        # let's finish with tau...
        # loop over the angles
        avg = []
        for ith in range(np.shape(costh)[0]):
            tmp=np.sum(np.sum(H[ith,:,:,:],axis=2),axis=1)
            tmp2 = tmp*bins_tau/m_ejecta[ith]
            avg.append(np.sum(tmp2))
        
        avg = np.asarray(avg)
        axs[2].plot(np.arccos(costh)*180/3.14159,avg,label=sim+crit_unbound)
        axs[2].set_xlabel(r'$\theta$')
        axs[2].set_ylabel(r'$\langle \tau \rangle$')
        axs[2].set_yscale('log')
        axs[2].set_ylim([1,100.])

        

        #plt.title('sim:'+sim+' crit:'+crit_unbound)

plt.legend()

plt.show()

    

    



