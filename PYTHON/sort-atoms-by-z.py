#!/usr/bin/bash

import numpy as np

numstruct = 27
numatom = 193
with open('all-pt4.xyz','r') as f:
    for i in range(numstruct):
        atomlist = []
        f.readline()
        name = f.readline()
        for j in range(numatom):
            tmp = f.readline()
            atomlist.append([ str(tmp.split()[0]),
                              float(tmp.split()[1]),
                              float(tmp.split()[2]),
                              float(tmp.split()[3])])
        atomlist_sorted = sorted(atomlist, key=lambda x : x[3])
#        print (new)
        with open('all-pt4-sorted.xyz','a') as g:
            g.write( '%6i\n' % (numatom))
            g.write( '%10s' % (name))
            for k in range(numatom):
                g.write( '%6s %16.8f %16.8f %16.8f\n' % (atomlist_sorted[k][0],atomlist_sorted[k][1],atomlist_sorted[k][2],atomlist_sorted[k][3]  ))
      
