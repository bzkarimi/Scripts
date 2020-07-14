#!/usr/bin/bash

import json
import numpy as np

num_structs = 26
g = json.load(open('./master/1.0/par_props.json.1', 'r'))
print (np.shape(g["0.0"]["displacements"]))

with open('final_dis','w') as f:
    for i in range(num_structs + 1):
        f.write('%-6s  %6s\n' % ('ID=',str(i)+".0"))
        for j in range(len(g[str(i)+".0"]["displacements"][i])):
            f.write('%-6s  %6i\n' % ('mode=',(j+1)))
            for k in np.arange(0, len(g[str(i)+".0"]["displacements"][j]), 3):
                f.write('%16.8f  %16.8f  %16.8f\n' %  
                       (g[str(i)+".0"]["displacements"][k], g[str(i)+".0"]["displacements"][k+1], g[str(i)+".0"]["displacements"][k+2]))
