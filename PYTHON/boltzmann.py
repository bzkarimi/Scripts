#!/usr/bin/env python

# Input energies are in hartree
# Output energies are in eV

import numpy as np

Eb = []

Epbe0_O   = -1.560571069    
Epbe_O    = -0.0573499
Epbe0_OH  = -7.555117044    
Epbe_OH   = -0.27764529
Epbe0_OOH = -13.26382114    
Epbe_OOH  = -0.48743619
beta300   = 1052.500401
beta1000  = 315.7501204
h_to_ev   = 27.2114

E_clust_tot = [-0.89943356, -0.89872604, -0.88912952, -0.88705845, -0.87586984, -0.87437244 ]
E_clust     = [-0.34504484 ]

exp300   = []
exp1000  = []
prob300  = []
prob1000 = []

for i in range(len(E_clust_tot)): 
    exp300.append( np.exp(-beta300 * (E_clust_tot[i] - min(E_clust_tot))) )
    exp1000.append( np.exp(-beta1000 * (E_clust_tot[i] - min(E_clust_tot))) )

prob300 = [icount / sum(exp300) for icount in exp300]
prob1000 = [icount / sum(exp1000) for icount in exp1000]

E_clust_totGM   = E_clust_tot[0]
E_clust_tot300  = sum([i*j for i,j in zip(E_clust_tot,prob300)])
E_clust_tot1000 = sum([i*j for i,j in zip(E_clust_tot,prob1000)])

print('prob clust+adsorbate')
print('300K:', prob300)
print('1000K:', prob1000)

exp300   = []
exp1000  = []
prob300  = []
prob1000 = []

for i in range(len(E_clust)): 
    exp300.append( np.exp(-beta300 * (E_clust[i] - min(E_clust))) )
    exp1000.append( np.exp(-beta1000 * (E_clust[i] - min(E_clust))) )

prob300 = [icount / sum(exp300) for icount in exp300]
prob1000 = [icount / sum(exp1000) for icount in exp1000]

print('prob clust')
print('300K:', prob300)
print('1000K:', prob1000)

E_clustGM   = E_clust[0]
E_clust300  = sum([i*j for i,j in zip(E_clust,prob300)])
E_clust1000 = sum([i*j for i,j in zip(E_clust,prob1000)])

Eb.append((E_clust_totGM - E_clustGM - Epbe_OOH)*h_to_ev)
Eb.append((E_clust_tot300 - E_clust300 - Epbe_OOH)*h_to_ev)
Eb.append((E_clust_tot1000 - E_clust1000 - Epbe_OOH)*h_to_ev)

print('GM', '300K', '1000K')
print(Eb)
